def process_file(inputFileName): # Processes a file and returns the dimensions and state
    inFile=open(inputFileName,"r")
    lines=inFile.readlines()
    d_line=lines[0].strip()
    dimensions=(int(d_line[0]),int(d_line[2]))
    state_pos={}
    state=()
    for i in range(16):
        ele_pos=int(lines[i+2])
        state_pos[ele_pos]=i
    for i in range(16):
        state+=(state_pos[i],)
    return dimensions,state

class H_calc():
    """ A class that calculates the weighted heuristic of a state"""
    def __init__(self,dimensions,state):
        self._dimensions=dimensions
        self._state=state
        self._nrows=int(dimensions[0]) 
        self._wheuristic=0
        self._Lheuristic=0
        self._halfheuristic1=0
        self._halfheuristic2=0
        for i in range(len(state)):
            tile_number=int(self._state[i])
            if tile_number ==0:
                continue
            current_row=i//self._nrows # get current row of each element
            current_column=i%self._nrows # get current column of each element
            current_position=(current_row,current_column) # store the current position as a tuple 
            goal_row=tile_number//self._nrows # gets the goal row of each element
            goal_column=tile_number%self._nrows # get goal column of each element
            goal_position=(goal_row,goal_column) # store goal position as tuple
            if goal_position==current_position: # if Current position is the goal position
                pass
            elif tile_number <= 7 :
                self._Lheuristic+=(abs((current_column)-(goal_column))+abs((current_row)-(goal_row)))*tile_number
                self._halfheuristic1+=(abs((current_column)-(goal_column))+abs((current_row)-(goal_row)))
            else:
                self._wheuristic+=(abs((current_column)-(goal_column))+abs((current_row)-(goal_row)))*tile_number #Apply heuristic calculation
                self._halfheuristic2+=(abs((current_column)-(goal_column))+abs((current_row)-(goal_row)))
        
    def get_dimensions(self):
        return self._dimensions

    def get_state(self):
        return self._state

    def get_nrows(self):
        return self._nrows

    def get_distance(self):
        return self._halfheuristic1 + self._halfheuristic2

    def get_wheuristic(self):
        return self._wheuristic

    def get_Lheuristic(self):
        return self._Lheuristic

    def get_heuristic(self):
        return self._wheuristic + self._Lheuristic

    def H_ratio(self):
        return self.get_heuristic()/self.get_distance()

    def H_prod(self):
        return self._Lheuristic*self._wheuristic

        
if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="input File of states and search type")
    parser.add_argument("-f","--inputFile",help="enter file name")
    # more parameters and they will be assigned to --state as a list.
    args = parser.parse_args()

info=process_file(args.inputFile)
Puzzle=H_calc(info[0],info[1])
h=Puzzle.get_heuristic()
d=Puzzle.get_distance()
wh=Puzzle.get_wheuristic()
lh=Puzzle.get_Lheuristic()
hr=Puzzle.H_ratio()
hp=Puzzle.H_prod()
#if d <= 35 and hr>3.6:
    #print("small distances:", d)
    #print("Corresponding heuristics:",h)
    #print("heuristic ratio:",hr)
#print("The wheuristic is:" ,wh)
#print("The lheuristic is:" ,lh)
print("The heuristic ratio is:" ,hr)
#print("the product of halves is", hp)
#print("heuristic:",h)
#print("distance:",d)
#print("difference:",(h-d))
#print("wh-d",(wh-d))

