# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧠 Task 1 — Print All Elements of an Array
    # Create a program that:
    # Creates an array (list) of 5 integers
    # Uses a for loop to print each element on a new line

# 📌 Requirements:
    # Use a list
    # Use a for loop
    # Do not use print(list) directly

array1 = [1, 3, 5, 10, 15]

for x in array1:
    print(x)


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")


# 🔢 Task 2 — Sum of Array Elements

# Write a program that:
    # Creates an array of numbers
    # Calculates the sum of all elements
    # Prints the result

# 📌 Requirements:
    # Use a for loop
    # Use an accumulator variable (total)
    # Do not use sum()

total = 0
list2 = list(range(10))

for x in list2:
    total += x

print(f"Total: {total}")

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Find the Largest Number in an Array

# Write a program that:
    # Creates an array (list) of integers
    # Finds and prints the largest number

# 📌 Requirements:
    # Use a for loop
    # Do not use max()
    # You may assume the list is not empty

list3 = [10, 15, 31, 2, 9, 7, 25]
max_value = list3[0]

for x in list3:
    if x > max_value:
        max_value = x

print(max_value)



print("____________End of Ex 3")