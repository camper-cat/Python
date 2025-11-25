# ============================== Start of Exercises
# ---------------- Task 1

print("__________Start of Ex 1")
# Task 1 — Managing a Fruit List

# 1) Create a list called fruits that contains:
# "apple", "banana", "cherry", "apple", "kiwi".
# 2) Add a new fruit (for example "orange") to the end of the list.
# 3) Insert "mango" at index 2 (before "cherry").
# 4) Remove all duplicates from the list (the final list should contain only unique fruits).
# 5) Print the final list and its length using len().

fruits = ["apple", "banana", "cherry", "apple", "kiwi"]
fruits.append("orange")
print(fruits)

fruits.insert(2, "mango")
print(fruits)

fruits.remove("apple")
print(fruits)
print(f"The len of fruits list =", len(fruits))
print()

# 4) Better:
unique_fruits = []
for f in fruits:
    if f not in unique_fruits:
        unique_fruits.append(f)

fruits = unique_fruits
print(fruits)

# or

unique_fruits = []
[unique_fruits.append(f) for f in fruits if f not in unique_fruits]
print(unique_fruits)
print(f"The len of fruits list =", len(unique_fruits))

print("_______End of Ex 1")
print()
# ------------The end of Task 1


# ---------------- Task 2
# Task 2 — Sorting and Reversing

# 1) Create a list of numbers called numbers:
# [23, 5, 100, 45, 67, 5, 23]

# 2) Sort the list in ascending order using .sort().
# 3) Create a copy of the sorted list (use .copy() or list() — not simple assignment).
# 4) Reverse the order of elements in the copied list.
# 5) Print both lists and observe the difference between them.
print("_________Start of Ex 2")

numbers = [23, 5, 100, 45, 67, 5, 23]
numbers.sort()
print(numbers)

numbers2 = numbers.copy()
numbers2.sort(reverse=True)
print(numbers2)

print("_________End of Ex 2")
print()
# ------------The end of Task 2


# ---------------- Task 3
# Task 3 — Creating a New List Using List Comprehension

# 1) Use the numbers list from the previous task (or create a new one).

# 2) Using list comprehension, create a new list called even_squares
# that contains the squares of only the even numbers from numbers.

# 3) Print this new list.

# 4) Extra: create another comprehension list called large_squares
# that contains the squares of numbers whose square is greater than 500.

print("_________Start of Ex 3")

numbers = [23, 5, 100, 44, 22, 12, 66, 45, 67, 5, 23]
even_squares = [x * x for x in numbers if x % 2 == 0]
print(even_squares)

large_squares = [x * x for x in numbers if x * x > 500]
print(large_squares)

print("_________End of Ex 3")

# ------------The end of Task 3

# ============================The end of Exercises
