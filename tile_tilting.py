import heapq
from copy import deepcopy
import numpy as np




class Tile:
    def __init__(self, tile:list, cost:int, path_cost:int = 0, move:str ="") -> None:
        self.tile = tile
        self.path_cost = path_cost  # G(n)
        self.cost = cost  # F(n) = H(n) + G(n)
        self.move = move  # storing move 
        self.children = []


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        self.index = 0

    def empty(self):
        return len(self.queue) == 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


class TileTilting:
    def __init__(self, initial:Tile, goal:list, goal_position:dict) -> None:
        self.initial = initial
        self.goal = goal
        self.goal_position = goal_position
        self.queue = PriorityQueue()
        self.visited = set()

    def matrix_shift(self, state, direction:str) -> np.ndarray:
        length, width = state.shape
        new_state = np.empty_like(state, dtype=object)
        new_state[:] = ""

        if direction == "r":
            for row in range(length):
                new_col = width - 1
                for col in range(width - 1, -1, -1):
                    if state[row][col] != "":
                        new_state[row][new_col] = state[row][col]
                        new_col -= 1

        elif direction == "l":
            for row in range(length):
                new_col = 0
                for col in range(width):
                    if state[row][col] != "":
                        new_state[row][new_col] = state[row][col]
                        new_col += 1

        elif direction == "d":
            for col in range(width):
                new_row = length - 1
                for row in range(length - 1, -1, -1):
                    if state[row][col] != "":
                        new_state[new_row][col] = state[row][col]
                        new_row -= 1

        elif direction == "u":
            for col in range(width):
                new_row = 0
                for row in range(length):
                    if state[row][col] != "":
                        new_state[new_row][col] = state[row][col]
                        new_row += 1

        return new_state

    def manhattan_distance(self, start, goal):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def find_positions(self, map):
        positions = {}
        
        for i, row in enumerate(map):
            for j, val in enumerate(row):
        
                if val:
                    if val not in positions:
                        positions[val] = []
        
                    positions[val].append((i, j))
        return positions

    def heuristic_func(self, map:np.ndarray) ->int:
        positions = self.find_positions(map)
        total_dist = 0
        for tile, start_positions in positions.items():
            if tile in self.goal_position:
        
                for start in start_positions:
                    min_distance = float('inf')
        
                    for goal in self.goal_position[tile]:
                        distance = self.manhattan_distance(start, goal)
        
                        if distance < min_distance:
                            min_distance = distance
        
                    total_dist += min_distance
    
        return total_dist # type:ignore

    def generator(self, state: Tile):
        for dir in ["r", "l", "u", "d"]:
            new_state = self.matrix_shift(deepcopy(state.tile), dir)
            # for checking by self.visited and preventing from repeated state and redundent path
          
            state_tuple = tuple(map(tuple, new_state)) 
            if state_tuple not in self.visited:
                new_tile = Tile(new_state, state.path_cost + self.heuristic_func(new_state), state.path_cost + 1, dir)
                self.queue.push(new_tile, new_tile.cost)
                self.visited.add(state_tuple)

    def evaluation(self, state:np.ndarray) -> bool:
        return np.array_equal(state, self.goal)

    def a_star(self) -> Tile|None:
        self.queue.push(self.initial, self.initial.cost)
        
        while not self.queue.empty():
            curr = self.queue.pop()
        
            if self.evaluation(curr.tile):
                print("success!")
                return curr
            
            self.generator(curr)
            print("Current State:")
            
            print(curr.tile)
            
            print("Move:", curr.move)
        print("No solution found")
        
        return None


def create_goal_positions(goal_map:np.ndarray) -> dict:
    goal_positions = {}
    for i, row in enumerate(goal_map):
        for j, val in enumerate(row):
            if val:
                if val not in goal_positions:
                    goal_positions[val] = []
                goal_positions[val].append((i, j))
    return goal_positions


map1 = np.array([
    ["", "r", "", ""],
    ["r", "g", "y", "b"],
    ["", "b", "", ""],
    ["", "y", "r", ""]], dtype=object)

goal = np.array([
    ["y", "r", "b", "r"],
    ["", "", "y", "r"],
    ["", "", "", "g"],
    ["", "", "", "b"]], dtype=object)

goal_positions = create_goal_positions(goal)

initial = Tile(map1, 0)

game = TileTilting(initial, goal, goal_positions)

result = game.a_star()
if result:
    print(f"Final State: {result.tile}")

else:
    print("no solution")
