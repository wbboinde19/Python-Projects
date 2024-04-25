"""download and/or process data"""
import torch
import torch.nn as nn
import torchaudio
import pandas as pd
from sonopy import power_spec, mel_spec, mfcc_spec, filterbanks


class MFCC(nn.Module):

    def __init__(self, sample_rate, fft_size=400, window_stride=(400, 200), num_filt=40, num_coeffs=40):
        super(MFCC, self).__init__()
        self.sample_rate = sample_rate
        self.window_stride = window_stride
        self.fft_size = fft_size
        self.num_filt = num_filt
        self.num_coeffs = num_coeffs
        self.mfcc = lambda x: mfcc_spec(
            x, self.sample_rate, self.window_stride,
            self.fft_size, self.num_filt, self.num_coeffs
        )
    
    def forward(self, x):
        return torch.Tensor(self.mfcc(x.squeeze(0).numpy())).transpose(0, 1).unsqueeze(0)


def get_featurizer(sample_rate):
    return torchaudio.transforms.MelSpectrogram(sample_rate=sample_rate, n_fft=400, win_length=400, hop_length= 200)


class RandomCut(nn.Module):
    """Augmentation technique that randomly cuts start or end of audio"""

    def __init__(self, max_cut=10):
        super(RandomCut, self).__init__()
        self.max_cut = max_cut

    def forward(self, x):
        """Randomly cuts from start or end of batch"""
        side = torch.randint(0, 1, (1,))
        cut = torch.randint(1, self.max_cut, (1,))
        if side == 0:
            return x[:-cut,:,:]
        elif side == 1:
            return x[cut:,:,:]


class SpecAugment(nn.Module):
    """Augmentation technique to add masking on the time or frequency domain"""

    def __init__(self, rate, policy=2, freq_mask=2, time_mask=1):
        super(SpecAugment, self).__init__()

        self.rate = rate

        self.specaug = nn.Sequential(
            torchaudio.transforms.FrequencyMasking(freq_mask_param=freq_mask),
            torchaudio.transforms.TimeMasking(time_mask_param=time_mask)
        )

        self.specaug2 = nn.Sequential(
            torchaudio.transforms.FrequencyMasking(freq_mask_param=freq_mask),
            torchaudio.transforms.TimeMasking(time_mask_param=time_mask),
            torchaudio.transforms.FrequencyMasking(freq_mask_param=freq_mask),
            torchaudio.transforms.TimeMasking(time_mask_param=time_mask)
        )

        policies = { 1: self.policy1, 2: self.policy2, 3: self.policy3 }
        self._forward = policies[policy]

    def forward(self, x):
        return self._forward(x)

    def policy1(self, x):
        probability = torch.rand(1, 1).item()
        if self.rate > probability:
            return  self.specaug(x)
        return x

    def policy2(self, x):
        probability = torch.rand(1, 1).item()
        if self.rate > probability:
            return  self.specaug2(x)
        return x

    def policy3(self, x):
        probability = torch.rand(1, 1).item()
        if probability > 0.5:
            return self.policy1(x)
        return self.policy2(x)


class WakeWordData(torch.utils.data.Dataset):
    """Load and process wakeword data"""

    def __init__(self, data_json, sample_rate=44100, valid=False):
        self.sr = sample_rate
        self.data = pd.read_json(data_json, lines=True)
        if valid:
            self.audio_transform = get_featurizer(sample_rate)
        else:
            self.audio_transform = nn.Sequential(torchaudio.transforms.MelSpectrogram(sample_rate=self.sr, n_fft= 400, win_length= 400, hop_length= 200, n_mels= 40),
                SpecAugment(rate=0.05)
            )

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.item()

        try:    
            file_path = self.data.key.iloc[idx]
            waveform, sr = torchaudio.load(file_path)
            # print(waveform)
            if sr > self.sr:
                waveform = torchaudio.transforms.Resample(sr, self.sr)(waveform)
            mfcc = self.audio_transform(waveform)
            num_frames = mfcc.shape[-1]
            num_frames_new = (num_frames // 40) * 40
            mfcc = mfcc[..., :num_frames_new]

            # Reshape the tensor to [* ,40]
            mfcc = mfcc.reshape(-1, 40)
            label = self.data.label.iloc[idx]

        except Exception as e:
            print(str(e), file_path)
            return self.__getitem__(torch.randint(0, len(self), (1,)))

        return mfcc, label


rand_cut = RandomCut(max_cut=10)

def collate_fn(data):
    """Batch and pad wakeword data"""
    mfccs = []
    labels = []
    """ Splits the data and puts mfccs and labels into separate lists
    the mfcc is squeezed and transposed"""
    for d in data:
        mfcc, label = d
        mfcc = mfcc.squeeze(0).transpose(0, 1)
        num_frames = mfcc.shape[-1]
        num_frames_new = (num_frames // 40) * 40
        mfcc = mfcc[..., :num_frames_new]

        # Reshape the tensor to [* ,40]
        mfcc = mfcc.reshape(-1, 40)
        mfccs.append(mfcc)
        labels.append(label)

    # pad mfccs to ensure all tensors are same size in the time dim
    
    mfccs = nn.utils.rnn.pad_sequence(mfccs, batch_first=True)  # batch, seq_len, feature
    mfccs = mfccs.transpose(0, 1) # seq_len, batch, feature
    mfccs = rand_cut(mfccs)
    # print(mfccs.shape)
    labels = torch.Tensor(labels)
    return mfccs, labels