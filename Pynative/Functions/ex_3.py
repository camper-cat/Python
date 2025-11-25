# Write a function calculation() that accepts two variables
# and calculates both their addition and subtraction.
# The function should then return both the sum and the difference
# in a single return statement.

def calculation(a, b):
    return a + b, a - b

print(calculation(40, 10))

# or

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
res = calculation(40, 10)
print(res)