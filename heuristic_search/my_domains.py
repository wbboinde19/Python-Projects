import sys
import math
class Sliding_Tile_Puzzle():
    """Domain for the sliding tile. This should take the dimensions of a tile and an input of
the intial state of all tiles and return information about it."""
    def __init__(self,dimensions,state):
        self._dimensions=dimensions
        self._state=state
        self._nrows=int(dimensions[0])
        self._i=self._state.index(0)
        self._current_0row=self._i//self._nrows # get current row of each element
        self._current_0column=self._i%self._nrows # get current column of each element
        self._current_0position=(self._current_0row,self._current_0column) # store the current position as a tuple 
        self._heuristic=0
        for i in range(len(state)):
            tile_number=int(self._state[i])
            if tile_number == 0:
                continue
            current_row=i//self._nrows # get current row of each element
            current_column=i%self._nrows # get current column of each element
            current_position=(current_row,current_column) # store the current position as a tuple 
            goal_row=tile_number//self._nrows # gets the goal row of each element
            goal_column=tile_number%self._nrows # get goal column of each element
            goal_position=(goal_row,goal_column) # store goal position as tuple
            if goal_position==current_position: # if Current position is the goal position
                pass
            else:
                self._heuristic+=(abs((current_column)-(goal_column))+abs((current_row)-(goal_row))) #Apply heuristic calculation

    def get_dimensions(self):
        return self._dimensions

    def get_state(self):
        return self._state

    def get_index(self,tile):
        s=self.get_state()
        i=s.index(int(tile))
        return i

    def get_nrows(self):
        return self._nrows

    def get_heuristic(self):
        return self._heuristic


    def swap(self,a,b): # a and b are indices. b>a
        S=self._state # Take the state from the terminal
        S=list(map(int,S)) # create new list of ints
        S[a],S[b]=S[b],S[a] # Swap values of the indices
        S=tuple(S)
        return S

    def get_0position(self):
        """ returns the position of zero in the state"""
        return self._current_0position

    def get_pmoves(self):
        """ Gets the movements that are posible by 0"""
        pos=self.get_0position()
        n=self.get_nrows()
        movements=()
        if pos==(0,(n-1)): # Top right corner
            movements+=(self.move_left(),self.move_down())
        elif pos==(0,0): # Top left corner
            movements+=(self.move_right(),self.move_down())
        elif pos[1]==0 and 0<pos[0]<(n-1): # left side
            movements+=(self.move_up(), self.move_down(),self.move_right())
        elif pos[1]==(n-1) and 0<pos[0]<(n-1): # right side
            movements+=(self.move_up(),self.move_down(),self.move_left())
        elif pos[0]==0 and 0<pos[1]<(n-1): # top side
            movements+=(self.move_left(),self.move_right(),self.move_down())
        elif pos[0]==(n-1) and 0<pos[1]<(n-1): # bottom side
            movements+=(self.move_left(),self.move_right(),self.move_up())
        elif pos==((n-1),0): # bottom left corner
            movements+=(self.move_up(),self.move_right())
        elif pos==((n-1),(n-1)): # bottom right corner
            movements+=(self.move_up(),self.move_left())
        else:
            movements+=(self.move_up(),self.move_down(),self.move_left(),self.move_right())
        return movements

    def move_up(self):
        """Moves the "0" tile up"""
        location=self.get_0position()
        if location[0]==0:
            return None
        else:
            n=self.get_nrows() # get the first element of the dimension
            i=self._i
            new_state=self.swap((i-n),i)
            new_puzzle=Sliding_Tile_Puzzle((n,n),new_state)
            #new_puzzle.print_puzzle()
            return new_puzzle

    def move_down(self):
        """Moves the 0 tile down"""
        location=self.get_0position()
        n=self.get_nrows()
        if location[0]==(n-1):
            pass
        else:
            i=self._i
            new_state=self.swap(i,(i+n))
            new_puzzle=Sliding_Tile_Puzzle((n,n),new_state)
            #new_puzzle.print_puzzle()
            return new_puzzle


    def move_left(self):
        """Moves the 0 tile left"""
        location=self.get_0position()
        n=self.get_nrows()
        if location[1]==(0):
            return None
        else:
            i=self._i
            new_state=self.swap((i-1),i)
            new_puzzle=Sliding_Tile_Puzzle((n,n),new_state)
            #new_puzzle.print_puzzle()
            return new_puzzle


    def move_right(self):
        """Moves the 0 tile right"""
        location=self.get_0position()
        n=self.get_nrows()
        if location[1]==(n-1):
            return None
        else:
            i=self._i
            new_state=self.swap(i,(i+1))
            new_puzzle=Sliding_Tile_Puzzle((n,n),new_state)
            #new_puzzle.print_puzzle()
            return new_puzzle

    def print_puzzle(self):
        rows= []
        row_start_index= 0
        row_end_index =self.get_nrows()-1
        for i in range(self.get_nrows()):
            rows.append(self.get_state()[row_start_index:(row_end_index+1)])
            row_start_index +=(self.get_nrows())
            row_end_index += self.get_nrows()
        for j in rows:
            print(j,sep=" ")

def move(state1,state2):
    """ reads the two states and returns the movements"""
    pos1=state1.get_0position()
    pos2=state2.get_0position()
    move=None
    if pos1[0]-1==pos2[0]:
        move="move_up"
    elif pos1[0]+1==pos2[0]:
        move="move_down"
    elif pos1[1]+1==pos2[1]:
        move="move_right"
    elif pos1[1]-1==pos2[1]:
        move="move_left"
    else:
        move=None
    return move
"""
if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sliding tile")
    parser.add_argument("-d","--dimensions",nargs=2,type=int, help="enter a tuple of the dimensions of the puzzle", required=True)
    parser.add_argument("-s","--state",nargs="+",type=int,help="enter the puzzle state",) # accepts one or
    # more parameters and they will be assigned to --state as a list.
    args = parser.parse_args()
    r_state=tuple(args.state)

Puzzle=Sliding_Tile_Puzzle(args.dimensions,r_state)
h=Puzzle.get_heuristic()
Puzzle.print_puzzle()
print("The heuristic is:" ,h) # print out the heuristic
moves=Puzzle.get_pmoves() # prints a list of posible states
print(moves)
print("taking first moves only")
for i in range(10):
    moves=Puzzle.get_pmoves()
    Puzzle=moves[1]
    Puzzle.print_puzzle()
    print("The heuristic of this puz is:",Puzzle.get_heuristic())
    """
