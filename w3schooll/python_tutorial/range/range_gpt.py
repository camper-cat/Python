# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧠 Task 1 — Print Numbers in a Range

# Write a program that:
    # Uses range()
    # Prints all numbers from 1 to 10 (inclusive), each on a new line

# 📌 Requirements:
    # Use a for loop
    # Do not create a list manually



for x in range(1, 11):
    print(x)


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")


# 🔢 Task 2 — Sum of Numbers in a Range

# Create a program that:
    # Uses range() to loop through numbers from 1 to 100
    # Calculates the sum of all numbers
    # Prints the result

# 📌 Requirements:
    # Use an accumulator variable (e.g. total)
    # range() must be the base of the loop

total = 0

for x in range(1, 101):
    total += x

print(f"Total: {total}")


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 📊 Task 3 — Print Only Even Numbers Using range

# Write a program that:
    # Uses range() with a step
    # Prints all even numbers from 2 to 20 (inclusive)

# 📌 Requirements:
    # Use range(start, stop, step)
    # Do not use if

for x in range(2, 21, 2):
    print(x)

print("____________End of Ex 3")