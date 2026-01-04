import math

# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧠 Task 1 — Absolute Value

# Write a program that:
    # Imports the math module
    # Takes a user input number (can be negative)
    # Prints the absolute value of that number using math.fabs()

number = int(input("Enter a number (can be negative): "))

print(f"Absolute value: {math.fabs(number)}")


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🔢 Task 2 — Ceiling and Floor

# Write a program that:
    # Imports the math module
    # Takes a floating point number from the user
    # Prints:
        # Ceiling of the number (math.ceil())
        # Floor of the number (math.floor())

number2 = float(input("Enter a float number: "))

ceilnumber = math.ceil(number2)
floornumber = math.floor(number2)

print(f"Ceil value: {ceilnumber}")
print(f"Floor value: {floornumber}")


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 📊 Task 3 — Power and Square Root

# Write a program that:
    # Imports the math module
    # Takes two numbers x and y from the user
    # Prints:
        # x raised to the power y using math.pow(x, y)
        # Square root of x using math.sqrt(x)

x = float(input("Enter x: "))
y = float(input("Enter y: "))

print(f"{x} to the power of {y} is: {math.pow(x,y)}")
print(f"Square root of {x} is: {math.sqrt(x)}")


print("____________End of Ex 3")