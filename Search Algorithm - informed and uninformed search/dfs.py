from collections import defaultdict
from queue import LifoQueue

class DFS:
    def __init__(self) -> None:
        self.visited = set()
        self.path = defaultdict(list)
        
    def add_node(self, vertex, edge):
        self.path[vertex].append(edge)
        
    def dfs_search(self, start):
        """recursive"""
        self.visited.add(start)
        print(start)
        
        for i in self.path[start]:
            if i not in self.visited:
                self.dfs_search(i)
                        

graph = DFS()
graph.add_node(0,1)
graph.add_node(0,2)
graph.add_node(1,2)
graph.add_node(2,0)
graph.add_node(2,3)
graph.add_node(3,3)

# graph.dfs_search(2)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< the main code >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


city_map = [
    [None, 1, None, None, None],
    [None, None, 1, None, None],
    [None, None, None, 1, None],
    [None, None, None, None, 1],
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
        self.frontier = LifoQueue()
        
    def generator(self, state: City):
        neighbor_city = city_map[city_guide.index(state.name)]
        
        for i in range(len(neighbor_city)):
            if neighbor_city[i]:
                temp = City(city_guide[i], state.path_cost + neighbor_city[i])
                self.frontier.put_nowait(temp)
                state.children.append(temp)
                break
                
                
    def evaluation(self, state: City):
        if state.name == self.goal:
            print(f"success! {state.path_cost}")
            return True
        return False
    
    def dfs(self) -> City:
        self.frontier.put_nowait(self.initial)
        
        while not self.frontier.empty():
            temp = self.frontier.get_nowait()
            
            if self.evaluation(temp):
                return temp
            
            self.generator(temp)
            
        
        
problem = Problem(City("A", 0), "E")

print(problem.dfs().name)
        
        
        