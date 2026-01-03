# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")


# Task 1 — Create a Greeting Function

# Write a program that:
    # 1) Defines a function called greet() that takes one parameter (a name).
    # 2) The function should print:
        # Hello, <name>! Nice to meet you!
        # Ask the user to enter their name.
        # Call the greet() function with the user’s name.

# 💡 Example interaction:
    # Input: Alice
    # Output: Hello, Alice! Nice to meet you!

name = input("Enter your name: ")

def greet(name):
    print(f"Hello, {name}! Nice to meet you!")
greet(name)

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🔢 Task 2 — Add Two Numbers Using a Function

# Create a program that:
    # Defines a function add_numbers(a, b) that returns the sum of two numbers.
    # Asks the user to enter two numbers.
    # Calls the function with these numbers and prints the result in a friendly message.

# 💡 Example output:
    # Enter first number: 5
    # Enter second number: 8
    # The sum is: 13


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add_numbers(a, b):
    return a + b

result = add_numbers(a, b)
print(f"The sum is: {result}")


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 📊 Task 3 — Function for a List Summary

# Write a program that:
    # Defines a function called list_summary(numbers) that:
        # Takes a list of numbers.
        # Returns the smallest number, the largest number, and the sum of all numbers.

    # In the main part of your program:
        # Ask the user to input numbers separated by spaces (like 3 7 10 12).
        # Convert the input into a list of integers.
        # Call list_summary() with this list.
        # Print each result clearly.

numbers_str = input("Enter numbers separated by spaces: ")
numbers_list = numbers_str.split()

numbers = []
for x in numbers_list:
    numbers.append(int(x))

def list_summary(numbers):

    def find_max(nums):
        if len(nums) == 1:
            return nums[0]
        max_rest = find_max(nums[1:])
        return nums[0] if nums[0] > max_rest else max_rest

    def find_min(nums):
        if len(nums) == 1:
            return nums[0]
        min_rest = find_min(nums[1:])
        return nums[0] if nums[0] < min_rest else min_rest

    def summ(nums):
        total = 0
        for x in nums:
            total += x
        return total

    max_value = find_max(numbers)
    min_value = find_min(numbers)
    sum_value = summ(numbers)

    return min_value, max_value, sum_value

result = list_summary(numbers)

print("The smallest number:", result[0])
print("The biggest number:", result[1])
print("The sum of all numbers:", result[2])
