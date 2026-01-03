# ======================================== Start of Exercises ===========================
# ---------------------------------------- Start of Ex 1 --------------------------------
# 🧩 Task 1 — “Calculations with Different Types”

# Description:

# Create the variables:

# x = 10       # int
# y = 3.5      # float


# Print the sum, difference, product, and division of these numbers in the format:

# Sum: 13.5
# Difference: 6.5


# (use f-strings or string concatenation)
# 3. Add comments for each operation.

x = 10       # int
y = 3.5      # float

print("Exercise 1:")
print("x =", x)
print("y =", y)
print(" ")

print("Sum: " + str(x + y))             # Using string concatenation
print("Sum:", x + y)
print(f"Sum: {x + y}")                  # Using f-strings
print(" ")

print("Difference: " + str(x - y))      # Using string concatenation
print("Difference:", x - y)
print(f"Difference: {x - y}")           # Using f-strings
print(" ")

print("Product: " + str(x * y))         # Using string concatenation
print("Product:", x * y)
print(f"Product: {x * y}")              # Using f-strings
print(" ")

print("Division: " + str(x / y))        # Using string concatenation
print("Division:", x / y)
print(f"Division: {x / y}")             # Using f-strings
print("The end of Exercise 1:")
print(" ")

# ---------------------------------------- End of Ex 1 --------------------------------

# ---------------------------------------- Start of Ex 2 --------------------------------
# 🧩 Task 2 — “Conversion and User Input”

# Description:

# Ask the user to enter two numbers using input().

# Convert the first number to int and the second to float.

# Print the types of both variables and their sum.

# Add comments explaining each step.

print("Exercise 2:")
number1 = (input("Enter the First number: "))                                   # Input number 1
number2 = (input("Enter the Second number: "))                                  # Input number 2
number1 = int(number1)                                                          # Convert to int
number2 = float(number2)                                                        # Convert to float
print("First number =", number1, ";" " it's has a type: ", type(number1))       # Print Variables and their type
print("Second number =", number2, ";" " it's has a type: ", type(number2))      # Print Variables and their type
print(f"Sum: {number1 + number2}")                                              # Print Sum of variables
print("The end of Exercise 2:")
print(" ")

# ---------------------------------------- End of Ex 2 --------------------------------

# ---------------------------------------- Start of Ex 2 --------------------------------
# 🧩 Task 3 — “Combining Numbers and Strings”

# Description:

# Create the variables:

# a = 7
# b = 2.5
# name = "Alice"

 # Print a message combining text and numbers, for example:

# Alice has 7 apples, each costs 2.5 dollars

# Calculate the total cost (a * b) and include it in the message.
a = 7
b = 2.5
name = "Alice"

print("Exercise 3:")
print(name, "has", a, "apples, each cost", b, "dollars")
print(f"The total cost: {a * b} dollars" )
print("End of Exercise 3:")

# ---------------------------------------- End of Ex 3 --------------------------------

# ======================================== End of Exercises ===========================