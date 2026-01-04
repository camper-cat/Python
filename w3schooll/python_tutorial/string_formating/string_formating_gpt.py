# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧪 Task 1 — Basic String Formatting

# Write a program that:
    # Asks the user for their name and age
    # Prints a message using f-string formatting, for example:
        # Hello Alice, you are 25 years old.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}, You are {age} years old.")

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — Format Numbers

# Write a program that:
    # Asks the user to enter a float number
    # Prints the number formatted to 2 decimal places using f-string formatting, for example:
        # Enter a number: 3.14159
        # Output: 3.14

number = float(input("Enter float number: "))

print(f"Output: {number:.2f}")

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 🧪 Task 3 — Multiple Variables in a String

# Write a program that:
    # Has three variables, for example:
        # product = "Laptop"
        # price = 899.99
        # quantity = 3

    # Prints a message using f-string formatting with all variables, for example:
        # You bought 3 Laptops for $899.99 each.

product = "Laptop"
price = 899.99
quantity = 3

print(f"You bought {quantity} {product}s for ${price} each.")


print("____________End of Ex 3")