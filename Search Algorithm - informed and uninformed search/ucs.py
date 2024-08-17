import heapq

city_map = [
    [None, 10, 12, None, None],
    [None, None, None, None, 8],
    [None, None, None, 1, None],
    [None, None, 1, None, 1],
    [2, None, None, None, None]
]
city_guide = ["A", "B", "C", "D", "E"]


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


class City:
    def __init__(self, name, cost) -> None:
        self.name = name 
        self.path_cost = cost 
        self.children = []
        
  
class Problem:
    def __init__(self, initial, goal) -> None:
        self.initial = initial
        self.goal = goal
        self.pq = PriorityQueue()
        
    def generator(self, state: City):
        neighbor_list = city_map[city_guide.index(state.name)]
        
        for i in range(len(neighbor_list)):
            if neighbor_list[i] != None:
                temp = City(city_guide[i], state.path_cost + neighbor_list[i])        
                self.pq.push(temp, temp.path_cost)
                state.children.append(temp)
                
    def evaluation(self, state: City):
        if self.goal == state.name:
            print(f"success! {state.path_cost}")
            return True
        return False
    
    def ucs(self) -> City:
        self.pq.push(self.initial, self.initial.path_cost)
        
        while not self.pq.empty():
            curr = self.pq.pop()
            
            if self.evaluation(curr):
                return curr
            
            self.generator(curr)
        
        
        
prob = Problem(City("A", 0), "E")
print(prob.ucs().name)
        
        
        
        
        