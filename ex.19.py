from queue import PriorityQueue
 

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []    
        self.parent = parent  
        self.value = value    
        self.dist = 0        
 
        if parent:
            self.start = parent.start   
            self.goal = parent.goal     
            self.path = parent.path[:]  
                                        
           
            self.path.append(value)     

        else:
            self.path = [value] 
            self.start = start  
            self.goal = goal   

    def GetDistance(self):
        pass
    def CreateChildren(self):
        pass
 
class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0 ):
        super(State_String, self).__init__(value, parent, start, goal) # create constructor
        self.dist = self.GetDistance() # override distance variable by calling GetDistance() method 
 
    def GetDistance(self):
           # first check to see if we have reached to our goal, and if we have then simply return 0  
            if self.value == self.goal:
                return 0
            dist = 0
 
           #Define a loop to go through each letter of the goal
            for i in range(len(self.goal)):
                letter = self.goal[i] # get the current letter
                
                dist += abs(i - self.value.index(letter)) #find index of letter in current value
                                                          #This will give the distance of letter is from its target p
            return dist   # simply return distance
 
#Define function to generate our children
    def CreateChildren(self):
            #if there are no children then go ahead and generate the children
            # this is just an extra precaution that we don't want to children twice 
 
            if not self.children:
                for i in range(len(self.goal)-1): # go through every possibilities or every possible arrangement of the letter.
                    val = self.value
 
                    # switching the second letter and the first letter of every pairs of letters
                    # and we track on the beginning and track on the end and then we have a new arrangement of letter in val.
                    val = val[:i] + val[i+1] + val[i] + val[i+2:]
 
                    # create a child and store the value of the child and pass self to store the parent of the child
                    child = State_String(val, self)
                    self.children.append(child)
class A_Star_Solver:
    def __init__(self, start, goal):
        self.path = []  # store final solution from start state to goal state
        self.vistedQueue =[] #it keeps track all the children that are visited
        self.priorityQueue = PriorityQueue()
        self.start = start  # store start state
        self.goal = goal    # store goal state
 
    def Solve(self):
        startState = State_String(self.start,0,self.start,self.goal) # it doesn't have any parent state. 
 
        count = 0
   
        # priorityQueue.put() is used to add children, you have to pass a tuple inside it.
        # The tuple contain 0, count and startState. 0 is priority number that we want
        self.priorityQueue.put((0,count, startState))
 
       # this while loop contain all the magic that is to be happenend
        while(not self.path and self.priorityQueue.qsize()):
               closesetChild = self.priorityQueue.get()[2]  # getting topmost value from the priority queue
               closesetChild.CreateChildren()    
               self.vistedQueue.append(closesetChild.value)  
               for child in closesetChild.children:
                   if child.value not in self.vistedQueue:
                    count += 1
                    if not child.dist:
                       self.path = child.path
                       break
                    self.priorityQueue.put((child.dist,count,child))
        if not self.path:
            print("Goal Of  is not possible !" + self.goal )
        return self.path
 if __name__ == "__main__":
    start1 = "hema"
    goal1 = "mahe"
    print("Starting....")
    a = A_Star_Solver(start1,goal1) 
    a.Solve()  
    for i in range(len(a.path)):    
        print("{0}){1}".format(i,a.path[i]))
from queue import PriorityQueue
 

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path[:]
            self.path.append(value)
 
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
 
    def GetDistance(self):
        pass
    def CreateChildren(self):
        pass
 
 

class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0 ):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDistance()
 
    def GetDistance(self):
            if self.value == self.goal:
                return 0
            dist = 0
            for i in range(len(self.goal)):
                letter = self.goal[i]
                dist += abs(i - self.value.index(letter))
            return dist
 
    def CreateChildren(self):
            if not self.children:
                for i in range(len(self.goal)-1):
                    val = self.value
                    val = val[:i] + val[i+1] + val[i] + val[i+2:]
                    child = State_String(val, self)
                    self.children.append(child)
 

class A_Star_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.vistedQueue =[]
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal
 
    def Solve(self):
        startState = State_String(self.start,0,self.start,self.goal)
 
        count = 0
        self.priorityQueue.put((0,count, startState))
        while(not self.path and self.priorityQueue.qsize()):
               closesetChild = self.priorityQueue.get()[2]
               closesetChild.CreateChildren()
               self.vistedQueue.append(closesetChild.value)
               for child in closesetChild.children:
                   if child.value not in self.vistedQueue:
                    count += 1
                    if not child.dist:
                       self.path = child.path
                       break
                    self.priorityQueue.put((child.dist,count,child))
        if not self.path:
            print("Goal Of  is not possible !" + self.goal )
        return self.path
 

if __name__ == "__main__":
    start1 = "hema"
    goal1 = "mahe"
    print("Starting....")
    a = A_Star_Solver(start1,goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("{0}){1}".format(i,a.path[i]))

