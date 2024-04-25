def process_file(inputFileName):
    inFile=open(inputFileName,"r")
    lines=inFile.readlines()
    d_line=lines[0].strip()
    dimensions=(int(d_line[0]),int(d_line[2]))
    print(dimensions)
    state_pos={}
    state=()
    for i in range(16):
        ele_pos=int(lines[i+2])
        state_pos[ele_pos]=i
    
    for i in range(16):
        state+=(state_pos[i],)
    print(state)
    return dimensions,state


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="input File of states")
    parser.add_argument("-f","--inputFile",help="enter file name")
    # more parameters and they will be assigned to --state as a list.
    args = parser.parse_args()

process_file(args.inputFile)