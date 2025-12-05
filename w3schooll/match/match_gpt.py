# ======================================== Start of Exercises ===========================

# ---------------------------------------- Start of Ex 1 --------------------------------
# 🔎 Practice Exercises – Python Match

# 1. Simple Calculator Using match-case

# Write a program that:
 # asks the user for two numbers (a and b),
 # asks for an operation (+, -, *, /),
 # uses match … case to choose and perform the operation,
 # prints the result,
 # prints an error message if the operation is unknown.

print("_______Ex 1")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")

print("_______The End of Ex 1")
print()

# ---------------------------------------- The end of Ex 1 --------------------------------

# ---------------------------------------- Start of Ex 2 --------------------------------

print("_______Ex 2")

# 2. Grade Description

# Create a function grade_description(grade)
# that takes a single-character string:
# "A", "B", "C", "D", "F" and returns a text description:
    # "A" → "Excellent"
    # "B" → "Good"
    # "C" → "Average"
    # "D" → "Below Average"
    # "F" → "Fail"
    # anything else → "Invalid grade"
 # Use match-case where each case handles one grade.
 # Use case _ for invalid input.


def grade_description():
    grade = input("Enter a mark: ")
    match grade:
        case "A":
            print("Excellent")
        case "B":
            print("Good")
        case "C":
            print("Average")
        case "D":
            print("Below Average")
        case "F":
            print("Fail")
        case _:
            print("Invalid grade")

grade_description()

print("_______The End of Ex 2")
print()

# ---------------------------------------- The end of Ex 2 --------------------------------

# ---------------------------------------- Start of Ex 3 --------------------------------

print("_______Ex 3")

# 3. Point Position (Tuple Pattern Matching)

# You have coordinates of a point in 2D space stored as a tuple (x, y).

# Write a function point_position(point) that:
    # receives a tuple point = (x, y),
    # uses match … case to check:
    # (0, 0) → "Point is at the origin"
    # (0, y) where y != 0 → "Point is on the Y axis"
    # (x, 0) where x != 0 → "Point is on the X axis"
    # anything else → "Point is in a quadrant"

x = int(input("Enter x: "))
y = int(input("Enter y: "))
point = (x, y)

def point_position(point):
    match point:
        case (0, 0):
            print("Point is at the origin")
        case (0, y) if y != 0:
            print("Point is on the Y axis")
        case (x, 0) if x != 0:
            print("Point is on the X axis")
        case _:
            print("Point is in a quadrant")

point_position(point)

