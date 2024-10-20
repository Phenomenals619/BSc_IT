def hill_climbing(f, x0, generate_neighbors):
    x = x0  # Initial solution
    while True:
        neighbors = generate_neighbors(x)  # Generate neighbors of x
        best_neighbor = max(neighbors, key=f)  # Find the neighbor with the highest function value
        if f(best_neighbor) <= f(x):  # If no improvement, stop
            return x
        x = best_neighbor  # Move to the best neighbor
        
print("Ahmed Shaikh 323")
# Example function to maximize
def example_function(x):
    return -x**2 + 4*x + 10

# Example neighbor generation function
def generate_neighbors(x):
    step_size = 0.1  # You can adjust the step size
    return [x - step_size, x + step_size]

# Initial guess
x0 = 0

# Running the hill climbing algorithm
best_solution = hill_climbing(example_function, x0, generate_neighbors)
print("Best solution:", best_solution)
print("Maximum value of f(x):", example_function(best_solution))
