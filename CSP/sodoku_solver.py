import time

from sympy import Domain
class Sudoku:
    def __init__(self, variables:list, domains:dict, constraints:dict) -> None:
        self.variable = variables
        self.domain = domains
        self.constraint = constraints
        self.solution = None

        
    def solve(self) -> dict:
        assignment = {}
        self.solution = self.backtrack_search_csp(assignment)
        return self.solution
    
    def select_unassigned_variable(self, assignment):
        # which variable should be assigned next (which is good for improving backtracking)
        # using MRV minimum-remaining-values
        # Time Complexity = O(n)
        
        min_values = float("inf")
        select_variable = None
        
        for var in self.variable:
            if var not in assignment:
                num_values = len(self.domain[var])
    
                if num_values < min_values:
                    min_values = num_values
                    select_variable = var

        return select_variable
            
        
    
    def order_domain_values(self, var, assignmet):
        # and what order should its values be tried to improve the backtrack
        # using least-constrainting-value
        # Time Complexity = O(d^2)
        # 1- usual code
        # return self.domain[var]
        
        # 2- LCV:
        counts = []
        for value in self.domain[var]:
            count = 0
            
            for neighbor in self.constraint[var]:
                if neighbor not in assignmet and value in self.domain[neighbor]:
                    count += 1
                    
            counts.append((value, count))
            
        ordered_values = [value for value, count in sorted(counts, key=lambda x: x[1])]
    
        return ordered_values
                
    
    def inference(self, value, var, assignment):
        # what inferences should be performed at each step in the search
        # using forward checking or maintaining-arc-consistency or shortcoming
        # time complexity = O(nd)
        # 1- forward checking:
        inferences = {}
        
        for neighbor in self.constraint[var]:
            if neighbor not in assignment:
                if value in self.domain[neighbor]:
                    remaining_values = [v for v in self.domain[neighbor] if v != value]
                    if not remaining_values:
                        return None
                    
                    else:
                        inferences[neighbor] = remaining_values

        return inferences
    
    def is_consistent(self, var, value, assignment):
        # O(n)
        for consistent_val in self.constraint[var]:
            if consistent_val in assignment and assignment[consistent_val] == value:
                return False
        return True
    
    def backtrack_search_csp(self, assignment):
        # O(n * d^n)
        # backjumping (which is not needed)
        if len(assignment) == len(self.variable):
            return assignment
        
        var = self.select_unassigned_variable(assignment)
        
        for value in self.order_domain_values(var, assignment):
            
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                inferences = self.inference(value, var, assignment)
                if inferences is not None:
                    old_domain = self.domain.copy()
                    self.domain.update(inferences)
                    
                    result = self.backtrack_search_csp(assignment)
                    if result is not None:
                        return result

                    self.domain = old_domain

                    del assignment[var]
        return None

# start = time.time()
puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
		[6, 0, 0, 1, 9, 5, 0, 0, 0], 
		[0, 9, 8, 0, 0, 0, 0, 6, 0], 
		[8, 0, 0, 0, 6, 0, 0, 0, 3], 
		[4, 0, 0, 8, 0, 3, 0, 0, 1], 
		[7, 0, 0, 0, 2, 0, 0, 0, 6], 
		[0, 6, 0, 0, 0, 0, 2, 8, 0], 
		[0, 0, 0, 4, 1, 9, 0, 0, 5], 
		[0, 0, 0, 0, 8, 0, 0, 0, 0] 
		] 

def print_sudoku(puzzle): 
	for i in range(9): 
		if i % 3 == 0 and i != 0: 
			print("- - - - - - - - - - - ") 
		for j in range(9): 
			if j % 3 == 0 and j != 0: 
				print(" | ", end="") 
			print(puzzle[i][j], end=" ") 
		print() 

  
# defining variables, variables in sudoku are all cells of the game which is 9*9 = 81 
    
variables = [(i, j) for i in range(9) for j in range(9)] 

    
# defining domains, values that can be assigned for variables whihc are 81 variables 
# all legal domains for a variable by it's position and neighbors value
Domains = {var: set(range(1, 10)) if puzzle[var[0]][var[1]] == 0 else {puzzle[var[0]][var[1]]} for var in variables} 


# defining constraints, constrains are rows and columns for (0,0) is row = 0 and all columns and
# column = 0 and all rows and numbers which were in sudoku before also the numbers in 3*3
# for (0,0) we have these:
# [(1, 0), (0, 1), (2, 0), (0, 2), (3, 0), (0, 3), (4, 0), (0, 4), (5, 0), (0, 5), (6, 0), (0, 6), (7, 0), (0, 7), (8, 0), (0, 8), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def add_constraint(var): 
	constraints[var] = [] 
	for i in range(9): 
		if i != var[0]: 
			constraints[var].append((i, var[1]))
    
		if i != var[1]: 
			constraints[var].append((var[0], i)) 
   
	sub_i, sub_j = var[0] // 3, var[1] // 3
	for i in range(sub_i * 3, (sub_i + 1) * 3): 
     
		for j in range(sub_j * 3, (sub_j + 1) * 3): 
			if (i, j) != var: 
				constraints[var].append((i, j)) 
				
constraints = {} 
for i in range(9): 
	for j in range(9): 
		add_constraint((i, j)) 



sudoku = Sudoku(variables, Domains, constraints) 
sol = sudoku.solve() 

# end = time.time()

solution = [[0 for i in range(9)] for i in range(9)] 

for i,j in sol: 
	solution[i][j]=sol[i,j] 
	
print_sudoku(solution)
# print((end - start) * 10 **3)
    
    
    
    