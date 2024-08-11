from collections import defaultdict
from queue import Queue

class BFS:
    def __init__(self) -> None:
        self.queue = []
        self.path = defaultdict(list)
        self.visited = set()
        
    def add_node(self, vertex, edge):
        self.path[vertex].append(edge)
    
    def bfs_search(self, start):
        self.queue.append(start)
        self.visited.add(start)
        
        while self.queue:
            node = self.queue.pop(0)
            print(node)
            
            for i in self.path[node]:
                if i not in self.visited:
                    self.queue.append(i)
                    self.visited.add(i)
                            
                    
graph = BFS()

graph.add_node(0,1)
graph.add_node(0,2)
graph.add_node(1,2)
graph.add_node(2,0)
graph.add_node(2,3)
graph.add_node(3,3)

# graph.bfs_search(2)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< the main code >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
city_map = [
    [None, 1, 1, None, None],
    [1, None, None, None, 1],
    [1, None, None, 1, 1],
    [None, None, 1, None, None],
    [None, 1, 1, None, None]
]
city_guide = ["A", "B", "C", "D", "E"]

class City:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.path_cost = cost
        self.children = []
        

class Problem:
    def __init__(self, initial, goal) -> None:
        self.initial = initial
        self.goal = goal
        self.frontier = Queue()
        
    def generator(self, state: City):
       neighbor_list = city_map[city_guide.index(state.name)]
       
       for i in range(len(neighbor_list)):
           if neighbor_list[i]:
                temp = City(city_guide[i], neighbor_list[i] + state.path_cost) 
                state.children.append(temp)
                self.frontier.put_nowait(temp)
                
    def evaluation(self, state: City):
        if state.name == self.goal:
            print(f"success with cost {state.path_cost}")
            return True
        return False
    
    def bfs(self) -> City:
        self.frontier.put_nowait(self.initial)
        
        while not self.frontier.empty():
            temp = self.frontier.get_nowait()
            
            if self.evaluation(temp):
                return temp
            
            self.generator(temp)
        
problem_city = Problem(City("A", 0), "E")    

print(problem_city.bfs().name)

