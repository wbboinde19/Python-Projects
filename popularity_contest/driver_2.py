import sys
import os.path

class Node():
    def __init__(self,domain_name,ref_count=1,parent=None,left=None,right=None):
        self._domain_name=domain_name
        self._ref_count=ref_count
        self._parent=parent
        self._left=left
        self._right=right

    def get_domain_name(self):
        return self._domain_name

    def get_ref_count(self):
        return self._ref_count

    def get_parent(self):
        return self._parent

    def get_left_child(self):
        return self._left

    def get_right_child(self):
        return self._right

    def set_domain_name(self,this):
        self._domain_name=this

    def set_ref_count(self,this):
        try:
            X=int(this)
        except:
            print("Hey your set is not right")
        self._ref_count=X

    def set_parent(self,this):
        self._parent=this

    def set_left_child(self, this):
        self._left=this

    def set_right_child(self, this):
        self._right=this

class binary_tree():
    def __init__(self):
        self._root=None
        self._size=0

    def get_root(self):
        return self._root

    def get_size(self):
        return self._size

    def set_root(self,this):
        self._root=this

    def is_root(self,p):
        return p.get_parent()==None

    def is_leaf(self,p):
        return p.get_left_child()==None and p.get_right_child()==None

    def add(self,data,p):
        if self.get_size()==0:
            new_node=Node(data,1)
            self._root=new_node
            self._size+=1
        #    print("root:",Tree._domain_name)
        else:
            while p:
                if p.get_domain_name()==data:
                    #print("Repeated:",Tree._domain_name)
                    p._ref_count+=1
                    return
                else:
                    for i in range(len(data)):
                        if ord(p.get_domain_name()[i])<ord(data[i]):
                            if p._right:
                                self.add(data,p._right)
                            else:
                                new_node=Node(data,1)
                                p._right=new_node
                                new_node._parent=p
                                self._size+=1
                            #    print("right:",Tree._right._domain_name)
                            return
                        if ord(p.get_domain_name()[i])>ord(data[i]):
                            if p._left:
                                self.add(data,p._left)
                            else:
                                new_node=Node(data,1)
                                p._left=new_node
                                new_node._parent=p
                                self._size+=1
                            #    print("left:",Tree._left._domain_name)
                            return

    def printInOrder(self,p):
        if p:
            self.printInOrder(p._left)
            print(p.get_domain_name(),p.get_ref_count())
            self.printInOrder(p._right)


def populate(inputlogfile,Tree):
    log=open(inputlogfile,"r")
    for line in log:
        domain_name=""
        for char in line:
            if char!=":":
                domain_name+=char
            else:
                break
        p=Tree.get_root()
        Tree.add(domain_name,p)
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

    Tree=binary_tree()
    populate(args.inputlogfile,Tree)
    p=Tree.get_root()
    Tree.printInOrder(p)
