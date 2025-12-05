# ======================================== Start of Exercises ===========================

# ---------------------------------------- Start of Ex 1 --------------------------------

# Exercise 1: Number Counter

# Description: Write a program that prints all numbers from 1 to 10 using a while loop.
# Hint:
 # Use a variable to store the current number.
 # Don’t forget to increase the counter inside the loop, otherwise it will run forever.

print("_______Ex 1")

number = 1

while number < 11:
    print(number)
    number += 1

print("_______The end of Ex 2")
print()

# ---------------------------------------- The end of Ex 1 --------------------------------

# ---------------------------------------- Start of Ex 2 --------------------------------
print("_______Ex 2")

# Exercise 2: Sum of User Input Numbers

# Description: Write a program that asks the user to enter numbers
# until they enter 0.
# After that, the program should print the sum of all entered numbers (excluding the 0).

# Hint:
 # Use input() to get user input.
 # Convert the input to int().
 # Keep a sum variable and add each number to it.

total = 0
number = int(input("Enter a number: "))

while number != 0:
    total += number
    number = int(input("Enter a number: "))

print("Sum of numbers:", total)

print("______The End of Ex 2")
print()

# ---------------------------------------- The end of Ex 2 --------------------------------


# ---------------------------------------- Start of Ex 3 --------------------------------

print("_______Ex 3")

# Exercise 3: Multiplication Table

# Description:
# Write a program that prints the multiplication table for a number
# entered by the user, from 1 to 10.

# Hint:
    # Use a while loop to count from 1 to 10.
    # Multiply the user number by the counter and print the result in the format:
    # number x counter = result

a = int(input("Enter a number from 1 to 10: "))
i = 1
while i <= 10:
    print(f"{a} * {i} = {a * i}")
    i += 1


