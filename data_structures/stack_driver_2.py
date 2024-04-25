import sys
import os.path
import copy
import myDataStructures_2 as myDat

def loadStack(inputFileName,Stack):
    inFile=open(inputFileName,"r")
    inFilelines=inFile.readlines()
    inFile.close()
    for x in inFilelines:
        try:
            intX=int(x.strip())
        except ValueError:
            print("The value was not an integer")
        Stack.push(intX)
    return Stack

def is_palindrome(Stack):
    Stack1=myDat.ListStack()
    Stack2compare=myDat.ListStack()
    for i in range(len(Stack)):
        Stack2compare.push(Stack.top())
        Stack1.push(Stack.top())
        Stack.pop()
    Stack2=myDat.ListStack()
    for l in range(len(Stack1)):
        Stack.push(Stack1.top())
        Stack2.push(Stack1.top())
        Stack1.pop()
    for k in range(len(Stack2)):
        for j in range(len(Stack2compare)):
            if not Stack2.top()==Stack2compare.top():
                return False
            Stack2.pop()
            Stack2compare.pop()
    return True

def reverseStack(Stack):
    Stack_reverse=myDat.ListStack()
    for i in range(len(Stack)):
        Stack_reverse.push(Stack.top())
        Stack.pop()
    return Stack_reverse

def count_sum(Stack):
    rStackcopy1=myDat.ListStack()
    Stackcopy1=myDat.ListStack()
    for l in range(len(Stack)):
        rStackcopy1.push(Stack.top())
        Stack.pop()
    for i in range(len(rStackcopy1)):
        Stackcopy1.push(rStackcopy1.top())
        Stack.push(rStackcopy1.top())
        rStackcopy1.pop()
    count=0
    sum=0
    for i in range(len(Stack)):
        sum+=Stackcopy1.top()
        count+=1
        Stackcopy1.pop()
    return count,sum

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Lab 6 - Stacks")
    parser.add_argument("-i","--inputFileName", type=str, help="File of integers, one per line", required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)

    Stack=myDat.ListStack()
    loadStack(args.inputFileName,Stack)

    rStackcopy1=myDat.ListStack()
    Stackcopy1=myDat.ListStack()
    for l in range(len(Stack)):
        rStackcopy1.push(Stack.top())
        Stack.pop()
    for i in range(len(rStackcopy1)):
        Stackcopy1.push(rStackcopy1.top())
        Stack.push(rStackcopy1.top())
        rStackcopy1.pop()

    is_palindrome(Stackcopy1)
    print(is_palindrome(Stackcopy1))

    rStackcopy1=myDat.ListStack()
    Stackcopy1=myDat.ListStack()
    for l in range(len(Stack)):
        rStackcopy1.push(Stack.top())
        Stack.pop()
    for i in range(len(rStackcopy1)):
        Stackcopy1.push(rStackcopy1.top())
        Stack.push(rStackcopy1.top())
        rStackcopy1.pop()

    Stack_reverse=reverseStack(Stackcopy1)

    print(is_palindrome(Stack_reverse))

    print(Stack_reverse.top())

    count_sum(Stack)
    print(count_sum(Stack))
