# ========================= Start of Exercises

# ----------- Task 1

# Exercise 1: Tuple Basics

# Goal: Practice creating tuples and accessing elements

# Instructions:
# 1) Create a tuple fruits containing the following fruits: "apple", "banana", "cherry".
# 2) Print the first and the last element of the tuple.
# 3) Try to change the second element of the tuple to "orange" and observe what happens.
# Hint: Tuples are immutable, which means you cannot change their elements.

print("________Start of Ex 1")

fruits = ("apple", "banana", "cherry")
print(fruits[0], fruits[-1])        # at one time
# or
print(fruits[-1])                   # singly
print()

# 3) to change second element i need to change Tuple in List 1st

fruits = list(fruits)
fruits[1] = "Orange"
fruits = tuple(fruits)
print(fruits)

print("________End of Ex 1")

# ----------- End of Task 1
print()

# ----------- Task 2

# Exercise 2: Iteration and Tuple Operations

# Goal: Practice looping through tuples and combining them

# Instructions:
# 1) Create a tuple numbers = (2, 4, 6, 8, 10).
# 2) Use a for loop to print each number squared.
# 3) Create another tuple more_numbers = (12, 14) and combine it with numbers into a new tuple all_numbers.
# 4) Print all_numbers and its length using len().
print("________Start of Ex 2")

numbers = (2, 4, 6, 8, 10)
for x in numbers:
    print(x ** 2)
print()

more_numbers = (12, 14)
all_numbers = numbers + more_numbers
print(f"All numbers: {all_numbers}", "its length is", len(all_numbers))

print("________End of Ex 2")
print()

# ------------ End of Task 2

# ------------ Start of Task 3

print("________Start of Ex 3")

#Exercise 3: Indexing and Tuple Methods

# Goal: Practice finding elements and using tuple methods

# Instructions:
 # 1) Create a tuple animals = ("cat", "dog", "rabbit", "dog").
 # 2) Count how many times "dog" appears in the tuple.
 # 3) Find the index of the first occurrence of "rabbit".
 # 4) Try using the append() method on the tuple and observe what happens.
 # Hint: Tuples have the methods count() and index(), but they do not support append() or remove().

animals = ("cat", "dog", "rabbit", "dog")

print(animals.count("dog"))

print(animals.index("rabbit"))

# to use .append() you need to change Tuple in List at 1st, .append(elevent), then rechange List to Tuple
# For example:

animals = list(animals)
animals.append("lion")
animals = tuple(animals)
print(animals)

# Or another way:

animals = ("cat", "dog", "rabbit", "dog")
lion = ("lion", )
animals += lion
print(animals)

print("________End of Ex 3")

print()