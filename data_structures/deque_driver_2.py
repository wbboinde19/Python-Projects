import sys
import os.path
class Deque():
    def __init__(self):
        self._deque=[]

    def __len__(self):
        return len(self._deque)

    def enqueueFront(self,element):
        self._deque.insert(0,element)

    def dequeueFront(self):
        if len(self._deque)==0:
            print("list is empty")
        else:
             element=self._deque[0]
             self._deque.pop(0)
        return element

    def enqueback(self,element):
        self._deque.append(element)

    def dequeueBack(self):
        if len(self._deque)==0:
            print("Hey your deque is empty")
        else:
            back=self._deque[len(self._deque)-1]
            self._deque.pop()
        return back

    def front(self):
        if len(self._deque)==0:
            print("Hey your deque is empty")
        else:
            return self._deque[0]

    def back(self):
        if len(self._deque)==0:
            print("Hey empty deque")
        else:
            return self._deque[len(self._deque)-1]

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Lab 6 - deques")
    parser.add_argument("-i","--inputFileName", type=str, help="File of integers, one per line", required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)

    mydeque=Deque()

    inFile=open(args.inputFileName,"r")
    inFilelines=inFile.readlines()
    inFile.close()
    for x in inFilelines:
        try:
            intX=int(x.strip())
        except ValueError:
            print("The value was not an integer")
        mydeque.enqueueFront(intX)
    print(len(mydeque))
    print(mydeque.front())
    print(mydeque.back())


    if len(mydeque)%2==0:
        ams=True
        for i in range(int(len(mydeque)/2)):
            if mydeque.front()!=mydeque.back():
                ans=False
                break
            mydeque.dequeueFront()
            mydeque.dequeueBack()
        print(ans)
    else:
        ans=True
        for j in range (int(len(mydeque)//2)):
            if mydeque.front()!=mydeque.back():
                ans=False
                break
            mydeque.dequeueFront()
            mydeque.dequeueBack()
        print(ans)
