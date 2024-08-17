class AustralliaMapColoring:
    def __init__(self, variables:list, domains:dict, constraints:dict) -> None:
        self.variable = variables
        self.domain = domains
        self.constraint = constraints
        self.solution = None

        
    def solve(self):
        assignment = {}
        self.ac_3()
        self.solution = self.backtrack_search_csp(assignment)
        return self.solution
    
    def ac_3(self):
        # O(n^2*d^3)
        queue = [(xi, xj) for xi in self.constraint for xj in self.constraint[xi]]
        while queue:
            (xi, xj) = queue.pop(0)
            
            if self.revise(xi, xj):
                if not self.domain[xi]:
                    return False
                for neighbor in self.constraint[xi]:
                    if neighbor != xj:
                        queue.append((neighbor, xi))
                        
        return True
        
    
    def revise(self, Xi, Xj):
        revised = False
        for x in self.domain[Xi][:]:
            if not any(self.satisfies(x, y) for y in self.domain[Xj]):
                self.domain[Xi].remove(x)
                revised = True
                
        return revised
    
    def satisfies(self, x, y):
        return x != y
    
    def select_unassigned_variable(self, assignment):
        # which variable should be assigned next (which is good for improving backtracking)
        # using MRV minimum-remaining-values
        # Time Complexity = O(n)
        # 1-
        
        # unassigned_var = [var for var in self.variable if var not in assignment]
        # return min(unassigned_var, key=lambda val: len(self.domain[val]))
        
        # 2- you can write like this but this is same as 1
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
        # var is variable
        for value in self.order_domain_values(var, assignment):
            # value is color
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                inferences = self.inference(value, var, assignment)
                if inferences is not None:
                    old_domain = self.domain.copy()
                    self.domain.update(inferences)
                    # print(self.domain)
                    result = self.backtrack_search_csp(assignment)
                    if result is not None:
                        return result

                    self.domain = old_domain

                    del assignment[var]
        return None

# model representation for AUSTRALIA MAP COLORING

# VARIABLE:
# X = {WA, NT, Q, NSW, V, SA, T}

# DOMAIN:
# D ={red, green, blue}. 

# CONSTRAINT:
# C = {SA != WA, SA != NT, SA != Q, SA != NSW, SA !=V, WA != NT, NT != Q, Q != NSW, NSW != V}

# Variables
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Domains
domains = {var: ['red', 'green', 'blue'] for var in variables}

# Constraints
constraints = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

csp = AustralliaMapColoring(variables, domains, constraints)
solution = csp.solve()
        
print(solution)