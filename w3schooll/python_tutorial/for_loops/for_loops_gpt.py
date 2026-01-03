# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")
# Task 1 — Count Letters in a Word

# Write a program that:
    # 1) Asks the user to enter a word.
    # 2) Uses a for loop to count how many times the letter "a" appears in the word.
    # 3) Prints the result.
        # 💡 Example:
        # Input: banana
        # Output: The letter "a" appears 3 times.

# ➡️ This task practices looping through a string.

word = input("Enter a word: ")
times = 0

for x in word:
    if x == "a":
        times += 1
print(f"The letter 'a' appears {times} times.")


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🔢 Task 2 — Multiplication Tables (1 to 10)

# Create a program that:
    # 1) Uses two nested for loops.
    # 2) Prints the multiplication table for numbers from 1 to 10.
    # 3) The output format should be:
        # 2 x 1 = 2
        # 2 x 2 = 4
        # ...
        # 2 x 10 = 20


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplier = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in numbers:
    for y in multiplier:
        print(f"{x} x {y} = {x * y}")
    print()

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Print Only Even Numbers

# Write a program that:
    # 1) Uses a list of numbers (for example: [3, 7, 10, 12, 15, 20]).
    # 2) Uses a for loop and the continue statement to print only even numbers.

list1 = [3, 7, 10, 12, 15, 20]

for x in list1:
    if x % 2 != 0:
        continue
    print(x)


print("____________End of Ex 3")
