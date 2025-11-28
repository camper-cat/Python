# ============================== Start of Exercises

# ------------------ Start of Task 1

print("________Start of Ex 1")
print()

# Exercise 1: Basics of Sets

# Goal: Practice creating sets and understanding uniqueness of elements

# Instructions:
 # 1) Create a set fruits with the following elements: "apple", "banana", "cherry", "apple".
 # 2) Print the set and observe what happens to duplicate elements.
 # 3) Check if "banana" is in the set using the in keyword.

fruits = {"apple", "banana", "cherry", "apple"}

print(fruits)               # duplicate elements doesn't output twice

if "banana" in fruits:
    print("Set 'fruits' has the value 'banana'")
else:
    print("Set 'fruits' has not the value 'banana'")

print()
print("________End of Ex 1")
print()

# ------------------- End of Ex 1

# -------------------- Start of Ex 2

print("________Start of Ex 2")
print()

# Exercise 2: Adding and Removing Elements

# Goal: Practice adding and removing elements from a set

# Instructions:
 # 1) Create a set numbers = {1, 2, 3, 4, 5}.
 # 2) Add the number 6 using the add() method.
 # 3) Remove the number 3 using the remove() method.
 # 4) Try to remove a number not in the set (e.g., 10) using discard() and observe the difference between remove() and discard().
 # 5) Print the final set.

numbers = {1, 2, 3, 4, 5}

numbers.add(6)
numbers.remove(3)
# numbers.remove(10)                .remove() method cannot be used if the set does not have a given value
numbers.discard(10)
print(numbers)
print()
print("________End of Ex 2")
print()

# ------------------ End of Ex 2

# -------------------- Start of Ex 3

print("________Start of Ex 3")
print()

# Exercise 3: Set Operations

# Goal: Practice common set operations: union, intersection, difference

# Instructions:
 # 1) Create two sets:
    # set_a = {1, 2, 3, 4}
    # set_b = {3, 4, 5, 6}
 # 2) Find and print the union of the sets.
 # 3) Find and print the intersection of the sets.
 # 4) Find and print the difference of set_a - set_b and set_b - set_a.
# Hint: Use operators: | (union), & (intersection), - (difference) or methods: .union(), .intersection(), .difference().

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Output № 1
print("first way")

union_set = set_a.union(set_b)

print(union_set)
print()

intersection_set = set_a.intersection(set_b)
print(intersection_set)
print()

difference_set1 = set_a.difference(set_b)
print(difference_set1)
difference_set2 = set_b.difference(set_a)
print(difference_set2)

print()

# Output № 2
print("Second way")

union = set_a | set_b
print(union)
print()

intersection = set_a & set_b
print(intersection)
print()

difference1 = set_a - set_b
print(difference1)
difference2 = set_b - set_a
print(difference2)

# ------------ The End of Ex 3

# ================= The End of Exercises
