# ======================================== Python Operators

"""
Operators are used to perform operations on variables and values.
"""

print(10 + 5)                   # + is Operator
print()

# Although the + operator is often used to add together two values,
# like in the example above, it can also be used to add together
# a variable and a value, or two variables:

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print()


# ====================================== Arithmetic Operators

"""
Arithmetic operators are used with numeric values to perform common mathematical operations:
"""

# Operator          	Name	                Example
# +	                    Addition	            x + y
# -	                    Subtraction	            x - y
# *	                    Multiplication	        x * y
# /	                    Division	            x / y
# %	                    Modulus	                x % y
# **	                Exponentiation	        x ** y
# //	                Floor division	        x // y

# Here is an example using different arithmetic operators:

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
print()


# ================================= Assignment Operators

"""
Assignment operators are used to assign values to variables:
"""

# Operator	            Example	                Same As
#   =	                x = 5	                x = 5
#   +=	                x += 3	                x = x + 3
#   -=	                x -= 3	                x = x - 3
#   *=	                x *= 3	                x = x * 3
#   /=	                x /= 3	                x = x / 3
#   %=	                x %= 3	                x = x % 3
#   //=	                x //= 3	                x = x // 3
#   **=	                x **= 3	                x = x ** 3
#   &=	                x &= 3	                x = x & 3
#   |=	                x |= 3	                x = x | 3
#   ^=	                x ^= 3	                x = x ^ 3
#   >>=	                x >>= 3	                x = x >> 3
#   <<=	                x <<= 3	                x = x << 3
#   :=	                print(x := 3)	        x = 3
#                                               print(x)

# -------------------- The Walrus Operator
# Python 3.8 introduced the := operator, known as the "walrus operator".
# It assigns values to variables as part of a larger expression:
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print()


# ============================ Comparison Operators

"""
Comparison operators are used to compare two values:
"""

# Operator	        Name	                    Example	Try it
#   ==	            Equal	                    x == y
#   !=	            Not equal	                x != y
#   >	            Greater than	            x > y
#   <	            Less than	                x < y
#   >=	            Greater than or equal to	x >= y
#   <=	            Less than or equal to	    x <= y

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print()

# -------- Chaining Comparison Operators
"""Python allows you to chain comparison operators:"""

x = 5

print(1 < x < 10)
print(1 < x and x < 10)
print()


# ================ Logical Operators

"""
Logical operators are used to combine conditional statements:
"""

# Operator	        Description	                                                    Example
# and 	            Returns True if both statements are true	                    x < 5 and  x < 10
# or	            Returns True if one of the statements is true	                x < 5 or x < 4
# not	            Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)

x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))
print()

# ================= Identity Operators

"""
Identity operators are used to compare the objects, 
not if they are equal, but if they are actually the same object, 
with the same memory location:
"""

# is 	            Returns True if both variables are the same object
# is not	        Returns True if both variables are not the same object

# The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)
print()

# ================== Membership Operators

"""
Membership operators are used to test if a sequence is presented in an object:
"""

# Operator	    Description
# in 	        Returns True if a sequence with the specified value is present in the object
# not in	    Returns True if a sequence with the specified value is not present in the object


# Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print()

#Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
print()

"""
The membership operators also work with strings:
"""

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
print()

# ================ Bitwise Operators

# Operator	    Name	                    Description	                                            Example
# & 	        AND	                        Sets each bit to 1 if both bits are 1	                x & y
# |	            OR	                        Sets each bit to 1 if one of two bits is 1	            x | y
# ^	            XOR	                        Sets each bit to 1 if only one of two bits is 1	        x ^ y
# ~	            NOT	                        Inverts all the bits	                                ~x
# <<	        Zero fill left shift	    Shift left by pushing zeros in from the right
#                                           and let the leftmost bits fall off	                    x << 2
# >>	        Signed right shift	        Shift right by pushing copies of the leftmost bit
#                                           in from the left, and let the rightmost bits fall off	x >> 2


# ================== Operator Precedence

"""
Operator precedence describes the order in which operations are performed.
"""

# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))
print()

# Multiplication * has higher precedence than addition +,
# and therefore multiplications are evaluated before additions:

print(100 + 5 * 3)
print()


"""
The precedence order is described in the table below, starting with the highest precedence at the top:
"""

# Operator	                                Description
# ()	                                    Parentheses
# **	                                    Exponentiation
# +x  -x  ~x	                            Unary plus, unary minus, and bitwise NOT
# *  /  //  %	                            Multiplication, division, floor division, and modulus
# +  -	                                    Addition and subtraction
# <<  >>	                                Bitwise left and right shifts
# &	                                        Bitwise AND
# ^	                                        Bitwise XOR
# |	                                        Bitwise OR
# ==  !=  >  >=  <  <=
# is  is not  in  not in
#                                           Comparisons, identity, and membership operators
# not	                                    Logical NOT
# and	                                    AND
# or	                                    OR

"""
if two operators have the same precedence, the expression is evaluated from left to right.
"""

print(5 + 4 - 7 + 3)
print()

