import sys
import os.path

class customer():
    """ A class that holds a customer name and a priority.
    Higher numbers are higher priority."""
    def __init__(self, name, priority):
        self._name=name
        self._priority=priority
        self._customer=(self._priority,self._name)

    def get_name(self):
        return self._name

    def get_priority(self):
        return self._priority

    def get_customer(self):
        return (self.get_priority(),self.get_name())


class priority_Queue():
    """ Holds items in order by priority and within priority by
    arrival time"""
    def __init__(self):
        self._queue=[] # Create an empty list

    def __len__(self):
        return len(self._queue)

    def create_customer(self,name,priority):
        person=customer(name,priority)
        return person.get_customer()

    def get_fist_customer(self):
        """ The first person is the one in the list with the highest
        priority"""
        # in the list we create, order doesn't matter
        if len(self._queue)==0:
            return "Hey no customer in the queue"
        max=self._queue[0] # max is a tuple
        index=0
        for i in range(1,len(self._queue)):
            if self._queue[i][0] > max[0]: # When you meet a value less than the recorded max
                max=self._queue[i] # change max to that value and keep track of the index
                index=i
        # Nothing will happen if we meet an element with same max or greater
        return max

    def get_last_customer(self):
        return self._queue[len(self._queue)-1]

    def get_customers(self,priority):
        """ This should get customers with given priority"""
        list=[]
        for i in range(self._queue):
            if self._queue[i][0]==priority:
                list.append(self._queue[i])
        return list

    def remove_first_customer(self):
        max=self._queue[0] # max is a tuple
        index=0
        for i in range(1,len(self._queue)):
            if max[0] < self._queue[i][0]: # When you meet a value less than the recorded max
                max=self._queue[i] # change max to that value and keep track of the index
                index=i
        # Nothing will happen if we meet an element with same max or greater
        self._queue.pop(index)

    def add_customer(self, person):
        """ person must be a tuple"""
        # check to see if customer exists first
        for customer in self._queue:
            if customer==person:
                return "customer already in queue"
        self._queue.append(person)

""" this implies that, to populate the queue, i just have to
get the name and priority of the customer and then create customer"""
def populate(inputFileName,Queue):
    """ reads a datafile of tuples and populates priority queue"""
    # From the file, romove the spaces in each line and spilt
    inFile=open(inputFileName,"r")
    for line in inFile:
        b=line.strip()
        b=b.replace(" ","")
        b=b.split(",") # this produces a list-name,priority
        try:
            str(b[0]) and int(b[1])
        except:
            print("Hey one of your customer info is in wrong format")
        Queue.add_customer(Queue.create_customer(str(b[0]),int(b[1])))
    inFile.close()
    return Queue


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Lab 9")
    parser.add_argument("-i","--inputFileName", type=str, help="File of domain names and priorities", required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)

    Queue=priority_Queue()
    populate(args.inputFileName, Queue )
    print(Queue.get_fist_customer()[1])
    Queue.remove_first_customer()
    print(Queue.get_fist_customer()[1])
    print(Queue.get_last_customer()[1])
