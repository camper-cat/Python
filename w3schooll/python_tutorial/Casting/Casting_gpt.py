# ======================================== Start of Exercises ===========================
# ---------------------------------------- Start of Ex 1 -----------------------------------

# 🧩 Task 1. Type Conversion for Calculations

# Goal: Learn how to convert strings to numbers and vice versa.

# Description:
# Create two variables:

# a = "15"
# b = "4"


# Convert them to numbers so that you can perform mathematical operations.

# Calculate their sum, difference, product, and division.

# Print the results in this format:

# Sum: 19
# Difference: 11
# Product: 60
# Division: 3.75

a = "15"                                    # Its str type
b = "4"                                     # Its str type

a = int(a)                                  # Convert from str to int
b = int(b)                                  # Convert from str to int

sum_result = a + b
difference = a - b
product = a * b
division = a / b

# Output
print("Exercise 1")
print(f"a = {a}, b = {b}")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Division: {division}")
print("The end of Exercise 2")
print()                                       # cleaner

# ---------------------------------------- End of Ex 1 --------------------------------


# ---------------------------------------- Start of Ex 2 -----------------------------------

# 🧩 Task 2. Casting Numbers to Strings for Output

# Goal: Understand how to combine numbers and strings for printing.

# Description:
# Create variables:

# name = "Alice"
# age = 25


# Print a sentence like:

# Alice is 25 years old.

# Use at least two different methods to combine text and numbers (for example, str() or f-strings).

name = "Alice"
age = 25

#Output
print("Exercise 2")
print(f"{name} is {age} years old")                 # Using f-string
print(name + "is " + str(age) + " years old")       # Using string concatenation
print("The end of Exercise 2")
print()                                             # cleaner


# ---------------------------------------- End of Ex 2 --------------------------------

# ---------------------------------------- Start of Ex 3 -----------------------------------

# 🧩 Task 3. Casting for Working with Floats and Integers

# Goal: Learn how to convert floats to integers and vice versa.

# Description:
# Create variables:

# x = 3.7
# y = 2


# Convert x to an integer and add it to y.

# Convert y to a float and multiply it by x.

# Print all results on the screen.

x = 3.7
y = 2

print("Exercise 3")
print(f"x = {x} and y = {y}")
print("x converted to int + y =", int(x) + y)                      # Convert x to int and + y
print("y converted to float * x =", float(y) * x)                  # Convert y to float and * x
print("The end of Exercise 3")
print()

# ---------------------------------------- End of Ex 2 --------------------------------


# ======================================== The end of Exercises ===========================