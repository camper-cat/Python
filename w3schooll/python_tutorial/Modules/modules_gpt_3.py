# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Import a Specific Function

# Write a program that:
    # Imports only the factorial function from math
    # Takes a user input number
    # Prints the factorial of that number using the imported function

# 📌 Requirements:
    # Use from math import factorial
    # Do not import the entire module

from math import factorial

number = int(input("Enter a number: "))
fact = factorial(number)

print(fact)


print("____________End of Ex 3")