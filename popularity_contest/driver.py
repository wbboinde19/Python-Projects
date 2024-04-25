import sys
import os.path

class Node():
    """ Creates a node with firlds for domain name, reference count and a pointer to the next node"""
    __slots__="_domain_name","_ref_count","_next"
    def __init__(self,domain_name,ref_count=1,next=None):
        self._domain_name=domain_name
        self._ref_count=ref_count
        self._next=next

class linked_list():
    """ A singly linked list containing information about a virtual domain"""
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def get_head(self):
        return self._head
    def get_tail(self):
        return self._tail
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def add(self,domain_name):
        if self.is_empty():
            newest=Node(domain_name) # this creates a new node with element
            # as the domain_name next as None with a reference count of 1
            self._head=newest
            self._tail=newest
            self._size+=1
        elif len(self)==1:
            newest=Node(domain_name)
            if self._head._domain_name==domain_name:
                self._head._ref_count+=1
            else:
                self._head._next=newest
                self._tail=newest
                self._size+=1
        else:
            newest=Node(domain_name)
            curr=self._head
            while curr:
                if curr._domain_name==domain_name:
                    curr._ref_count+=1
                    newest=None
                    return
                else:
                    curr=curr._next
            self._tail._next=newest
            self._tail=newest
            self._size+=1

    def total_ref_count(self,curr):
        if curr==self._tail:
            return self._tail._ref_count
        else:
            return curr._ref_count+self.total_ref_count(curr._next)

    def unique_domain_num(self):
        count=0
        curr=self._head
        while curr:
            count+=1
            curr=curr._next
        return count

    def most_popupular(self):
        max=self._head._ref_count
        domain_name=self._head._domain_name
        curr=self._head
        while curr:
            if max<curr._ref_count:
                max=curr._ref_count
                domain_name=curr._domain_name
            elif domain_name!=curr._domain_name and max==curr._ref_count:
                domain_name+=", "+curr._domain_name
                max=curr._ref_count
            curr=curr._next
        return domain_name, max

    def percentage_visit(self,domain_name):
        curr=self._head
        total=self.total_ref_count(curr)
        ref=0
        while curr:
            if curr._domain_name==domain_name:
                ref=curr._ref_count
                break
            curr=curr._next
        percent=str(int(((float(ref)/float(total))*100)))+"%"
        return percent

def populate(inputlogfile,list):
    log=open(inputlogfile,"r")
    for line in log:
        domain_name=""
        for char in line:
            if char!=":":
                domain_name+=char
            else:
                break
        list.add(domain_name)
    log.close()
    return list


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Lab 7")
    parser.add_argument("-i","--inputlogfile", type=str, help="File of domain names", required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputlogfile)):
        print("error,", args.inputlogfile, "does not exist, exiting.", file=sys.stderr)
        exit(-1)

    list=linked_list()
    populate(args.inputlogfile,list)
    print(list.total_ref_count(list.get_head()))
    print(list.unique_domain_num())
    print(list.most_popupular()[0],list.most_popupular()[1])
    print(list.percentage_visit(list.most_popupular()[0]))
