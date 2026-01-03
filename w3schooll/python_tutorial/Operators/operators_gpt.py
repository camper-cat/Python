# ============================== Start of Exercises

"""
Start of Ex 1
"""

# Task 1: Mini Calculator with Arithmetic Operators

# Create a program that works like a small text-based calculator:

# Ask the user to enter two numbers (x and y).
# Print the results of applying all arithmetic operators from W3Schools:
# +, -, *, /, %, **, //

# Format the output like:

# x + y = …
# x - y = …
# x * y = …
# ...

# If y is zero, handle division safely (avoid errors).

# Output:
print("______ Start of Ex 1")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x ** y = {x ** y}")

if y == 0:
    print("Cannot divide by zero for /, //, and % operators")
else:
    print(f"x / y = {x / y}")
    print(f"x // y = {x // y}")
    print(f"x % y = {x % y}")

print("_______ End of Ex 1")
print()

"""
End of Ex 1
"""

"""
Start of Ex 2
"""
print("_______ Start of Ex 2")
# Task 2: Value Comparison + Logical Operators

# Write a program that:

# 1. Gets three numbers: a, b, c.
# 2. Checks and prints the results of these comparisons:

# a > b
# b <= c
# a == c

# 3. Combine these comparisons using logical operators:

# If a > b and b <= c → print "Condition 1 and 2 are true"
# If a == c or b == c → print "Some values are equal"
# If not (a > b) → print "a is not greater than b"

# Output:
a = float(input("Enter the 'a' number: "))
b = float(input("Enter the 'b' number: "))
c = float(input("Enter the 'c' number: "))

print(f"a > b - it's: {a > b}")
print(f"b <= c - it's: {b <= c}")
print(f"a = c - it's: {a == c}")
print()

if a > b and b <= c:
    print("Condition 1 and 2 are true")
else :
    print("Condition 1 and 2 are false")

if a == c or b == c:
    print("Some values are equal")
else:
    print("Some values are not equal")

if not(a > b):
    print("a is not greater than b")
else:
    print("a is greater than b")

print("_______ End of Ex 2")
print()

"""
End of Ex 2
"""


"""
Start of Ex 3
"""

print("_______ Start of Ex 3")

# Task 3: Assignment Operators in Action

# Write a program that demonstrates how assignment operators work.

# 1. Create a variable:
 # x = 10

# 2. Apply several assignment operators step by step:
 # x += 5
 # x *= 2
 # x //= 3
 # x **= 2

# 3. After each operation, print the current value of x.

# 4. Optional (if your Python supports it):
 # Demonstrate the walrus operator :=  :

 # y = 3
 # if (y := y + 2) > 4:
 #     print("y is now", y)

# x = float(input("Enter 'x' number: "))
# x1 = x
# x2 = x
# x3 = x
# x4 = x
#
# # print(f"x += 5 - it's {x += 5} ")               # SyntaxError: f-string: expecting '=', or '!', or ':', or '}'
#
# x1 += 5
# print(f"x += 5 - it's {x1}")
#
# x2 *= 2
# print(f"x *= 2 - it's {x2}")
#
# x3 //= 3
# print(f"x //= 3 - it's {x3}")
#
# x4 **= 2
# print(f"x **= 2 - it's {x4}")

# Output № 2

x = float(input("Enter 'x' number: "))

temp = x
temp += 5
print(f"x += 5 -> {temp}")

temp = x
temp *= 2
print(f"x *= 2 -> {temp}")

temp = x
temp //= 3
print(f"x //= 3 -> {temp}")

temp = x
temp **= 2
print(f"x **= 2 -> {temp}")

print()

# Second part of Ex 3

y = 3
if (y := y + 2) > 4:
    print(f"y was 3 and now -> {y}")

print("_______ End of Ex 3")
