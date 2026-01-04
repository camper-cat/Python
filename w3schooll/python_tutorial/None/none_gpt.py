# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧪 Task 1 — Assign None to a Variable

# Write a program that:
    # Creates a variable x and assigns it the value None
    # Prints the variable
    # Prints the type of the variable

x = None

print(x)
print(type(x))

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — Function Returning None

# Write a program that:
    # Creates a function greet() that prints a greeting but does not return anything
    # Calls the function and assigns its result to a variable result
    # Prints the value of result (should show None)

def greet():
    print("Hello")
    return

result = greet()

print(result)

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 🧪 Task 3 — Check for None
 
# Write a program that:
    # Creates a variable data = None
    # Uses an if statement to check if the variable is None
        # If it is None, prints "No data available"
        # Otherwise, prints "Data exists"

data = None

if data is None:
    print("No data available")
else:
    print("Data exists")


print("____________End of Ex 3")