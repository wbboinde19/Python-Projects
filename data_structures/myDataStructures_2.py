class ListStack():
    """ Uses Python list a underlying storage medium to buil a stack"""
    def __init__(self):
        """ creates an empty list"""
        self._myStack=[]

    def __len__(self):
        return len(self._myStack)

    def push(self,e):
        """ Adds e to the rear of the stack"""
        self._myStack.append(e)

    def pop(self):
        self._myStack.pop() # check to see if it will raise error when the stack is empty?

    def top(self):
        """ Views the last element in the list"""
        return self._myStack[len(self._myStack)-1]


class ListQueue():
    """ Use Python list as the underlying storage medium to create a queue"""
    def __init__(self):
        self._myqueue=[]

    def __len__(self):
        return len(self._myqueue)

    def enqueue(self,e):
        self._myqueue.append(e)

    def dequeue(self):
        element=self._myqueue[0]
        self._myqueue.pop(0)

    def front(self):
        return self._myqueue[0]


if __name__=="__main__":
    Stack=ListStack()
    print(len(Stack))
    Stack.push(1)
    Stack.push(3)
    print(Stack.top())
    print(len(Stack))
    Stack.pop()
    print(len(Stack))

    Queue=ListQueue()
    print(len(Queue))
    Queue.enqueue(9)
    print(len(Queue))
    Queue.enqueue(7)
    print(Queue.front())
    print(len(Queue))
    Queue.dequeue()
    print(len(Queue))
    print(Queue.front())
