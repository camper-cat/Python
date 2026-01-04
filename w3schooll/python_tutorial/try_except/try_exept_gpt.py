# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")


# 🧪 Task 1 — Handle Division by Zero

# Task:

# Write a program that:
    # Asks the user to enter two numbers
    # Divides the first number by the second number
    # Uses try...except to handle division by zero
    # If there is no error, prints the result
    # If the second number is 0, prints:
        # You cannot divide by zero

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

try:
    print(number1/number2)
except ZeroDivisionError:
    print("You can't divide by zero")



print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — Handle Invalid Integer Input

# Write a program that:
    # Asks the user to enter a value
    # Tries to convert the value to an integer
    # Uses try...except to handle invalid input
    # If the input is valid, prints:
        # You entered: <number>
    # If the input is not a number, prints:
        # Invalid input


value1 = input("Enter a value: ")

try:
    value1 = int(value1)
    print(f"You entered {value1}")
except ValueError:
    print("Invalid input")


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 🧪 Task 3 — Access List Element Safely

# Write a program that:
    # Creates a list, for example:
        # numbers = [10, 20, 30, 40]
    # Asks the user to enter an index
    # Tries to print the element at that index
    # Uses try...except to handle an invalid index
    # If the index is out of range, prints:
        # Index out of range

numbers = [10, 20, 30, 40]
index = int(input("Enter an index: "))

try:
    print(numbers[index])
except IndexError:
    print("Index out of range")


print("____________End of Ex 3")

# --------------------- End of Ex 2

# ---------------------- Start of Ex 4
print("____________Start of Ex 4")
#
# # 🧪 Task 1 — Positive Number Input
#
# # Write a program that:
#     # Asks the user to enter a number
#     # Uses try...except to check that the input is an integer
#     # Uses raise to throw a ValueError if the number is less than or equal to 0
#     # Uses else to print a message if the number is valid
#     # Uses finally to print "End of program" no matter what

try:
    pos_number = int(input("Enter a number: "))
    if pos_number <= 0:
        raise ValueError("Number must be positive")
except ValueError as ve:
    print(f"You entered an invalid number: {ve}")
else:
    print(f"You entered a positive number: {pos_number}")
finally:
    print("End of program")