from chemeq import chemeq

# Define the unbalanced equation as a string
# Use " = " or " -> " to separate reactants and products
unbalanced_equation = "H2 + O2 -> H2O"

# Create a chemeq object
eq = chemeq(unbalanced_equation)

# Balance the equation
eq.balance()

# Print the balanced equation (the library handles formatting)
print(f"Unbalanced: {unbalanced_equation}")
print(f"Balanced: {eq}")

# Another example: a complex combustion reaction
unbalanced_equation_2 = "C4H10 + O2 -> CO2 + H2O"
eq2 = chemeq(unbalanced_equation_2)
eq2.balance()
print(f"\nUnbalanced: {unbalanced_equation_2}")
print(f"Balanced: {eq2}")