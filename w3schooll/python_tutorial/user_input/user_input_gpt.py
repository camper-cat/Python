# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧪 Task 1 — Simple Input

# Write a program that:
    # Asks the user to enter their name
    # Prints a greeting using the entered name

name = input("Enter your name: ")

print(f"Hello, {name}")

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — Input and Convert

# Write a program that:
    # Asks the user to enter a number
    # Converts the input to an integer
    # Prints the square of the number

number2 = int(input("Enter a number: "))

print(f"Square: {number2**2}")

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 🧪 Task 3 — Multiple Inputs

# Write a program that:
    # Asks the user to enter two numbers separated by space
    # Converts them to integers
    # Prints their sum and product

numbers = input("Enter a numbers separated by space: ")
numbers = list(numbers.split())

num1 = int(numbers[0])
num2 = int(numbers[1])

print(f"Sum: {num1+num2}")
print(f"Product: {num1*num2}")



print("____________End of Ex 3")