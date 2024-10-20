from constraint import Problem

# Create a new CSP problem
problem = Problem()

# Variables: regions of the map
variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Domain: colors available (Red, Green, Blue)
domain = ["Red", "Green", "Blue"]

# Add variables to the problem with their domain
problem.addVariables(variables, domain)

# Constraints: adjacent regions cannot have the same color
problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))
problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
problem.addConstraint(lambda a, b: a != b, ("SA", "V"))
problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
problem.addConstraint(lambda a, b: a != b, ("NSW", "V"))

# Solve the problem
solutions = problem.getSolutions()

# Print the solutions
print(f"Number of solutions: {len(solutions)}")
for solution in solutions:
    print(solution)
