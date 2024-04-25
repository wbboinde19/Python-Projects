import sys
import os.path
import cProfile
import my_domains as Domain
import heap
""" Domain should take inputs of dimensions and state"""
class A_star_Node():
    """ A node containing the list of tile number arrangement, their hueristics and pointers to children"""
    def __init__(self,state_node,heuristic=None,priority=None,Parent=None,Err_h=0):
        self._state_node=state_node
        self._heuristic=heuristic
        self._Parent=Parent
        self._priority=priority
        self._Err_h=Err_h

        if Parent!=None:
            self._distance=Parent.get_distance()+1
        else:
            self._distance=0
        self._state=self._state_node.get_state()

    def __lt__(self,Other):
        if self.get_priority()<Other.get_priority():
            return True
        elif self.get_priority()==Other.get_priority() and self.get_heuristic()<Other.get_heuristic():
            return True
        else:
            return False

    def __eq__(self, other):
        if other==None:
            return False
        return self.get_state()==other.get_state()

    def __hash__(self):
        return hash(self._state)
    
    def get_state(self):
        return self._state

    def get_state_node(self):
        return self._state_node

    def get_heuristic(self):
        return self._heuristic

    def get_Parent(self):
        return self._Parent

    def get_priority(self):
        return self._priority

    def get_distance(self):
        return self._distance

    def get_Err_h(self):
        return self._Err_h

    def is_goal(self):
        return self.get_heuristic()==0

    def get_mov_opt(self):
        """ Takes a state and asks the Domain for Children"""
        children=self.get_state_node().get_pmoves()
        return children




def A_star_search(initial_state):
    """ A* search algorithm"""
    """ initial_state is an object of the start state of the Domain"""
    Close={} # A dictionary for visited nodes
    Open=heap.heap([]) # A queue for all nodes to be visited
    nodes_expanded=0
    nodes_duplicated=0
    Err_h=0
    Sum_of_Err_h=0
    meanErr=0
    Start_Node=A_star_Node(initial_state,initial_state.get_heuristic(),(initial_state.get_heuristic() + 0)) # starting node/root
    nodes_generated=1
    Open.push(Start_Node)
    while not Open.is_empty(): # while the dictionary is not empty
        current_node=Open.pop()
        if current_node.is_goal(): # if the current node you got from the queue is the goal
            path=[] # Create and empty path
            while current_node!=Start_Node: # until the current node you are on is the Start node
                path.append(current_node.get_state()) # append the current node in the path
                current_node=current_node.get_Parent() # move to the parent of that node
            path.append(Start_Node.get_state()) # append the start node
            path=path[::-1] # reverse the path
            """ At this point, the path is a list of nodes."""
            print("Total nodes generated:",nodes_generated)
            print("Total nodes expanded:",nodes_expanded)
            print("Total nodes duplicated:",nodes_duplicated)
            print("The sum of h Error data:", Sum_of_Err_h)
            return path
        else: # If the current node is not the goal
            C=current_node.get_mov_opt() # gets all the possible children
            nodes_expanded+=1
            # I need to get the best child here apply the heuristic correction.
                #loop through the children and get the child with least f
            bch_p_index=0
            bch_p=C[bch_p_index]
            bch_p_h=bch_p.get_heuristic()
            for intg in range(len(C)):
                if C[intg].get_heuristic()<bch_p_h:
                    bch_p_index=intg
                    bch_p=C[bch_p_index]
                    bch_p_h=bch_p.get_heuristic()
                
                #calculate the heuristic error of this step
                #Get the mean error here
                #use the errors to calculate a new heuristic of the best child
            
            for i in range(len(C)): # for each posible direction
                child=C[i]
                if child==bch_p:
                    H_Error=(current_node.get_heuristic()-1)-child.get_heuristic() # Gives the error of the child generated
                    print(H_Error)
                    Sum_of_Err_h+=H_Error
                    meanErr=(Sum_of_Err_h/nodes_expanded)
                    Nw_hrstc=child.get_heuristic()/(1-meanErr)
                else:
                    Nw_hrstc=child.get_heuristic()
                node=A_star_Node(child,Nw_hrstc,(Nw_hrstc + current_node.get_distance()+1),current_node)
                nodes_generated+=1 
                # with parent as the curent node
                if child.get_state() in Close: # if the node already exists in the closed list
                    nodes_duplicated+=1
                    cl_node=Close[child.get_state()]
                    nodes_duplicated+=1
                    if (current_node.get_distance()+1)>=cl_node.get_distance():
                        continue
                    else:
                        Open.push(node)
                        Close.pop(child.get_state())
                elif node in Open: # if the state exists in the Open
                    nodes_duplicated+=1
                    pos=Open[node]
                    if (current_node.get_distance()+1)>=pos.get_distance():
                        continue
                    else:
                        Open[pos]=node
                else:
                    Open.push(node) # add each child into the open dictionary
        Close[current_node.get_state()]=current_node # add the visited node to the dictionary
    return []

def process_file(inputFileName):
    inFile=open(inputFileName,"r")
    lines=inFile.readlines()
    d_line=lines[0].strip()
    dimensions=(int(d_line[0]),int(d_line[2]))
    state_pos={}
    state=()
    for i in range(9):
        ele_pos=int(lines[i+2])
        state_pos[ele_pos]=i
    for i in range(9):
        state+=(state_pos[i],)
    return dimensions,state


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="input File of states and search type")
    parser.add_argument("-f","--inputFile",help="enter file name")
    parser.add_argument("-t","--type",type=str,help="input the search type")
    # more parameters and they will be assigned to --state as a list.
    args = parser.parse_args()

if args.type == "a_star":
    info=process_file(args.inputFile)
    Puzzle=Domain.Sliding_Tile_Puzzle(info[0],info[1])
    h=Puzzle.get_heuristic()
    print(end="\n")
    print("initial state:")
    Puzzle.print_puzzle()
    print(end="\n")
    print("The heuristic is:" ,h) # print out the heuristic
    print(end="\n")
    P=A_star_search(Puzzle)
    print(end="\n")
    print("Tile movements:")
    index=0
    Move_list=[]
    if len(P)==0:
        print("Goal not reached")
    else:
        for i in range(len(P)-1):
            S1=Domain.Sliding_Tile_Puzzle(info[0],P[i])
            #S1.print_puzzle()  
            S2=Domain.Sliding_Tile_Puzzle(info[0],P[i+1])            
            Move_list.append((Domain.move(S1,S2)))
            index=i
        print(Move_list)
        print(end="\n")
        print("Number of tile movements to reach goal:",index+1)

