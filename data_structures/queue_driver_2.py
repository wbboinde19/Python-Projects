import sys
import os.path
import copy
import myDataStructures_2 as myDat

def loadqueue(inputFileName,queue):
    inFile=open(inputFileName,"r")
    inFilelines=inFile.readlines()
    inFile.close()
    for x in inFilelines:
        try:
            intX=int(x.strip())
        except ValueError:
            print("The value was not an integer")
        queue.enqueue(intX)
    return queue

def queue_is_palindrome(queue):
    queue1=myDat.ListQueue()
    queue2compare=myDat.ListQueue()
    stack=myDat.ListStack()
    for i in range(len(queue)):
        queue2compare.enqueue(queue.front())
        queue1.enqueue(queue.front())
        queue.dequeue()
    stack=myDat.ListStack()
    queue=myDat.ListQueue()
    for l in range(len(queue1)):
        stack.push(queue1.front())
        queue.enqueue(queue1.front())
        queue1.dequeue()
    queue1=myDat.ListQueue()
    for z in range(len(queue)):
        queue1.enqueue(stack.top())
        stack.pop()
    for k in range(len(queue1)):
        for j in range(len(queue2compare)):
            if not queue1.front()==queue2compare.front():
                return False
            queue1.dequeue()
            queue2compare.dequeue()
    return True

def reverseQueue(queue):
    queue1=myDat.ListQueue()
    for i in range(len(queue)):
        queue1.enqueue(queue.front())
        queue.dequeue()
    stack=myDat.ListStack()
    queue=myDat.ListQueue()
    for l in range(len(queue1)):
        stack.push(queue1.front())
        queue.enqueue(queue1.dequeue())
    queue1=myDat.ListQueue()
    for j in range(len(stack)):
        queue1.enqueue(stack.top())
        stack.pop()
    return queue1

def count_sum(queue):
    qcount=0
    qsum=0
    queue1=myDat.ListQueue()
    for z in range(len(queue)):
        queue1.enqueue(queue.front())
        queue.dequeue()
    stack=myDat.ListStack()
    queue=myDat.ListQueue()
    for l in range(len(queue1)):
        stack.push(queue1.front())
        queue.enqueue(queue1.front())
        queue1.dequeue()
    queue1=myDat.ListQueue()
    for j in range(len(stack)):
        queue1.enqueue(stack.top())
        stack.pop()
    for i in range(len(queue)):
        qsum+=(queue1.front())
        qcount+=1
        queue1.dequeue()
    return qcount,qsum

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Lab 6 - Queues")
    parser.add_argument("-i","--inputFileName", type=str, help="File of integers, one per line", required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)

    queue=myDat.ListQueue()
    loadqueue(args.inputFileName,queue)
    queue1=myDat.ListQueue()
    for i in range(len(queue)):
        queue1.enqueue(queue.front())
        queue.dequeue()
    disque=myDat.ListQueue()
    queue=myDat.ListQueue()
    for l in range(len(queue1)):
        disque.enqueue(queue1.front())
        queue.enqueue(queue1.front())
        queue1.dequeue()
    print(queue_is_palindrome(disque))

    queue1=myDat.ListQueue()
    for i in range(len(queue)):
        queue1.enqueue(queue.front())
        queue.dequeue()
    disque=myDat.ListQueue()
    queue=myDat.ListQueue()
    for l in range(len(queue1)):
        disque.enqueue(queue1.front())
        queue.enqueue(queue1.front())
        queue1.dequeue()

    queue_reverse=reverseQueue(disque)
    print(queue_is_palindrome(queue_reverse))
    print(queue.front())
    print(count_sum(queue))
