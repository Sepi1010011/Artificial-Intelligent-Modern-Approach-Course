import heapq
import copy
import time


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        self.index = 0
        
    def empty(self):
        if self.index == 0:
            return True
        return False
        
    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index += 1
        
    def pop(self):
        return heapq.heappop(self.queue)[-1]
    


class Puzzle:
    def __init__(self, value:list, cost, path_cost=0) -> None:
        self.value = value # List
        self.cost = cost # F(n) = H(n) + G(n)
        self.path_cost = path_cost # G(n)
        self.children = []
        
        
class EightPuzzle:
    def __init__(self, initial, goal) -> None:
        self.initial:Puzzle = initial 
        self.goal:list = goal 
        self.frontier = PriorityQueue()
    
    def swap(self, puzzle:list, path_cost:int, pos, newpos):
        
        puzzle[pos[0]][pos[1]], puzzle[newpos[0]][newpos[1]] = puzzle[newpos[0]][newpos[1]], puzzle[pos[0]][pos[1]]      
        newstate = Puzzle(puzzle, path_cost + 1 + self.manhattan_distance(puzzle), path_cost + 1)
        
        return newstate
    
    def manhattan_distance(self, state:list):
        
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    index = [(index, row.index(state[i][j])) for index, row in enumerate(self.goal) if state[i][j] in row][0]
                    distance += abs(index[0] - i) + abs(index[1] - j)    
        return distance
    
    def generator(self, state: Puzzle):

        zero_index = [(index, row.index(0)) for index, row in enumerate(state.value) if 0 in row][0]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  

        for move in moves:
            newpos = (zero_index[0] + move[0], zero_index[1] + move[1])
            if 0 <= newpos[0] < 3 and 0 <= newpos[1] < 3: 

                state_new = self.swap(copy.deepcopy(state.value), state.path_cost, zero_index, newpos)

                self.frontier.push(state_new, state_new.cost)

    def evaluation(self, state: Puzzle):
        if self.goal == state.value:
            print(f"Success! {state.path_cost}")
            return True
        return False
    
    def a_star(self):
        self.frontier.push(self.initial, self.initial.path_cost)
        
        while not self.frontier.empty():
            curr = self.frontier.pop()

            if self.evaluation(curr):
                return curr
            
            self.generator(curr)
        
        
        
start = [
    [7,2,4],
    [5,0,6],
    [8,3,1]
]

# start = [
#     [1,0,2],
#     [3,4,5],
#     [6,7,8]
# ]
       
goal = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]        
s = time.time()  
puzzle = EightPuzzle(Puzzle(start,0), goal)
puzzle.a_star()  
end = time.time()
print(end - s,"s", "time to find answer")
        
        
        
        
        
        
        
        