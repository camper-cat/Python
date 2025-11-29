# ============================= Start of Exercises

# ---------------------- Task 1

print("__________Start of Ex 1")
print()

# ✅ Task 1 — Check if a Number is Even or Odd

# Write a program that:
    # 1) takes an integer number from the user,
    # 2) checks whether the number is even or odd,
    # 3) prints a message like:
        # “The number X is even”
        # or “The number X is odd”.
# Hint: Use % 2 to check evenness.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

print()
print("__________End of Ex 1")

# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 1

print("__________Start of Ex 2")
print()

# ✅ Task 2 — Age Verification (Voting Eligibility)
#
# Write a program that:
    # 1) asks the user for their age (integer),
    # 2) if the age is 18 or above, print:
        # “You are allowed to vote.”
    # otherwise print:
    # “You are too young.”
# A classic basic if ... else example.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are allowed to vote")
else:
    print("You are too young")

print()
print("__________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3

print("__________Start of Ex 3")
print()

# ✅ Task 3 — Temperature Category

# Write a program that:
    # 1) takes a temperature value from the user (integer or float),
    # 2) prints one of the following messages depending on the temperature:
        # if temperature > 25 → “It’s hot”
        # elif temperature > 15 → “It’s warm”
        # else → “It’s cold or cool”

# This helps you practice if … elif … else.

temp = int(input("What temperature is today? : "))

if temp > 25:
    print("It's hot")
elif temp > 15:
    print("It's warm")
else:
    print("It's cool")

