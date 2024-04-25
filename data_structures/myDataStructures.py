import dynamic_array as da
class ArrayStack():
    """ LIFO stack implementation using dynamicArray as undelying storage"""
    def __init__(self):
        """ Creates an empty stack"""
        self._Sdata=da.DynamicArray() # this creates an Array of cap 1 and len 0

    def __len__(self):
        """ Returns the length of self._data"""
        return len(self._Sdata) # this will use the magic fucntion in DynamicArray to read
# the len of self._n

    def is_empty(self):
        """ Returns true if len == 0 and false if otherwise """
        return len(self._Sdata)==0

    def push(self,e):
        """ Adds e to the rear of the stack """
        self._Sdata.append(e) # this doubles the capacity if full and puts e in the
# rear and then it adds one to self._n.

    def pop(self):
        """ removes the rear element"""
        self._Sdata.remove_index(len(self)-1)

    def top(self):
        """ Views the rear element """
        if self.is_empty():
            print("No element to top")
        else:
            return self._Sdata[len(self)-1]


class ArrayQueue():
    """ FIFO queue implementation using dynamicArray"""
    def __init__(self):
        """ creates an empty queue with capacity 10"""
        self._Qdata=da.DynamicArray()
        self._Qdata._resize(10)
        self._front=0

    def __len__(self):
        return len(self._Qdata)

    def is_empty(self):
        return len(self._Qdata)==0

    def front(self):
        if self.is_empty():
            print("There is nothing in the Queue")
        else:
            return self._Qdata[self._front]

    def dequeue(self):
        if self.is_empty():
            print("Hey there is nothing in the queue")
        else:
            element=self.front()
#            if self._front<len(self._Qdata):
            self._Qdata.remove_index(self._front)
            self._front=(self._front+1)% self._Qdata.cap()
#            else:
#                self._Qdata.remove_index(self._front)
#                self._front=(self._front)% (len(self._Qdata))
            return element

    def enqueue(self,element):
        """Adds an elementto the rear of the queue"""
        self._Qdata.append(element)



if __name__=="__main__":
    Stack=ArrayStack()
    print(len(Stack))
    Stack.push(1)
    Stack.push(3)
    print(Stack.top())
    print(len(Stack))
    Stack.pop()
    print(len(Stack))

    Queue=ArrayQueue()
    print(len(Queue))
    Queue.enqueue(9)
    print(Queue.is_empty())
    print(len(Queue))
    Queue.enqueue(7)
    print(Queue.front())
    print(len(Queue))
    Queue.dequeue()
    print(len(Queue))
    print(Queue.front())
