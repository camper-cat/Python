# ========================== Start of Exercises =====================

"""
Start of Ex 1
"""

print("         Ex 1")

#🧩 Task 1: Age check

# Write a program that:

# asks the user (using input()) for their age (as an integer)
# checks if the user is 18 years old or older
# prints a message:

# if age ≥ 18 → "You are an adult"
# otherwise → "You are underage"

# also prints the Boolean value of the condition (True or False).

age = input("Enter you age: ")
age = int(age)

if age >= 18:
    print("You are an adult")
else:
    print("You are underage")

print(bool(age >= 18))

print()

"""
End of Ex 1
"""

"""
Start of Ex 2
"""
print("     Ex 2")
#🧩 Task 2: Empty or not empty string

# Write a program that:

# defines a variable s manually in your code (for example s = "" or s = "Hello").
# uses the function bool() to check whether the string is empty or not.
# prints a message:

# if s is not empty → "The string contains characters"
# if s is empty → "The string is empty"
# additionally, print the Boolean value returned by bool(s).

s = "asdasd"

if s:
    print("The string contains characters")
else:
    print("The string is empty")
print(bool(s))
print()

"""
End of Ex 2
"""

"""
Start of Ex 3
"""

print("     Ex 3")
# 🧩 Task 3: Checking a combined condition

# Write a program that:

# defines two variables a and b (integers) manually
# checks whether both conditions are true: a > 0 and b > 0 (both numbers are positive)

# prints a message:
# if both are positive → "Both numbers are positive"
# if at least one is not positive → "At least one number is not positive"
 # also prints the Boolean result (True or False).

# then test with different values of a and b
# (e.g., -5 and 3, 4 and 0, 10 and 20) and observe how the result changes.

a = 10
b = -5

if a > 0 and b > 0:
    print("Both numbers are positive")
else:
    print("At least one number is not positive")

print(bool(a > 0 and b > 0))

"""
End of Ex 3
"""

# ============================== End of Exercises