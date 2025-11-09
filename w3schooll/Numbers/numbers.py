# ============================================ Python Numbers ===============================
# There are three numeric types in Python:

# --- int
# --- float
# --- complex

# Variables of numeric types are created when you assign a value to them:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print("                 Python numbers")
print("x = ", x, ";", "type of x variable: ", type(x))
print("y = ", y, ";", "type of y variable: ", type(y))
print("z = ", z, ";", "type of z variable: ", type(z))
print(" ")

# ------------------------------------ Int ------------------------------------------
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print("                 Int (Integer)")
print("x = ", x, ";", "type of x variable: ", type(x))
print("x = ", x, ";", "type of x variable: ", type(x))
print("y = ", y, ";", "type of y variable: ", type(y))
print("z = ", z, ";", "type of z variable: ", type(z))
print(" ")

# ----------------------------------- Float --------------------------------------------
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

print("                 float (Float)")
print("x = ", x, ";", "type of x variable: ", type(x))
print("y = ", y, ";", "type of y variable: ", type(y))
print("z = ", z, ";", "type of z variable: ", type(z))
print(" ")

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print("             Scientific numbers with an 'e'")
print("x = ", x, ";", "type of x variable: ", type(x))
print("y = ", y, ";", "type of y variable: ", type(y))
print("z = ", z, ";", "type of z variable: ", type(z))
print(" ")

# --------------------------------- Complex --------------------------------------
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print("                 Complex numbers")
print("x = ", x, ";", "type of x variable: ", type(x))
print("y = ", y, ";", "type of y variable: ", type(y))
print("z = ", z, ";", "type of z variable: ", type(z))
print(" ")

# ========================================= Type Conversion ==========================================
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print("                 Type Conversion")
print("x = ", x, ";", "type of x variable: ", type(x))
print("y = ", y, ";", "type of y variable: ", type(y))
print("z = ", z, ";", "type of z variable: ", type(z))
print("a = ", a, ";", "type of a variable: ", type(a))
print("b = ", b, ";", "type of b variable: ", type(b))
print("c = ", c, ";", "type of c variable: ", type(c))
print(" ")

# Note: You cannot convert complex numbers into another number type.

# ------------------------------------- Random Number --------------------------------------------
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

# Import the random module, and display a random number from 1 to 9:
import random

print("                     Random module")
print(random.randrange(1, 10))
print(" ")

# ================================== The end ============================== 
