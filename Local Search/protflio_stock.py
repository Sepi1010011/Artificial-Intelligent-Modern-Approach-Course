import numpy as np
import copy

LAMBDA = 0.5
RESTART_NUM = 600


def hill_climbing(r, covariance, base_weights):
    current_weights = base_weights
    while True:
        neighbors = get_neighbors(r, covariance, current_weights)
        if not neighbors:
            break  
        nei_scale = []
        for i in range(len(neighbors)):
            scale = formula(neighbors[i][0], neighbors[i][1], neighbors[i][2])
            nei_scale.append(scale)   
            
        next_weights = max(nei_scale)

        if np.all(formula(next_weights, r, covariance) <= formula(current_weights, r, covariance)):
            break

        current_weights = next_weights

    return current_weights

def get_neighbors(r, covariance, weights):
    stocks = [weights, r, covariance]
    neighbors = []
    
    for i in range(len(weights)):
        new_neighbors = copy.deepcopy(stocks)
        new_neighbors[0][i] = weights[i] + np.random.uniform(-0.1, 0.1)
        new_neighbors[0][i] /= np.sum(new_neighbors[0]) # for nomalization
        neighbors.append(new_neighbors)

    return neighbors

def formula(weights, r, covariance_matrix):
    return np.dot(np.array(weights).T, r) - LAMBDA * np.sqrt(np.dot(np.array(weights).T, np.dot(np.cov(covariance_matrix), weights)))

def random_restart_hill_climbing(r, base_weights, covariance):
    
    best_weights = hill_climbing(r, covariance, base_weights)

    weights = [0] * len(best_weights)
    counter = 0
    for _ in range(RESTART_NUM):
        for i in range(len(weights)):
            weights[i] = np.random.uniform(len(best_weights)) # type:ignore
            weights[i] = weights[i] / np.sum(weights) # for nomalization

        solution = hill_climbing(r, covariance, weights)
        if np.all(formula(solution, r, covariance) > formula(best_weights, r, covariance)):
            best_weights = solution
        
        counter += 1
            
    return best_weights, counter

def run(stocks):
    print(random_restart_hill_climbing(stocks[2], stocks[0], stocks[3]))
    
# stocks = [
#   [0.49, 0.32, 0.56],
#   [100, 50, 200],
#   [0.15, 0.1, 0.02],
#   [0.05, 0.03, 0.01]
# ]

if __name__ == "__main__":
    num_stock = int(input("Enter Number of Stacks: "))
    stocks = np.zeros((4, num_stock))
    
    for i in range(num_stock):

        initial_weights = np.random.random(1)[0]
        price = input("Enter the price of stock: ")
        profit = input("Enter the profit of stock: ")
        risk = input("Enter the risk of stock: ")
        for j in range(4):
            stocks[j][i] = initial_weights
            stocks[j][i] = price
            stocks[j][i] = profit
            stocks[j][i] = risk
        
    run(stocks)