# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧠 Task 1 — Basic Iterator

# Write a program that:
    # Creates a list: [1, 2, 3, 4, 5]
    # Creates an iterator for the list
    # Uses next() to print the first three elements of the list

# 📌 Requirements:
    # Use iter() and next()
    # Do not use a for loop

list1 = [1, 2, 3, 4, 5]

listit = iter(list1)

print(next(listit))
print(next(listit))
print(next(listit))


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🔢 Task 2 — Loop Through an Iterator

# Write a program that:
    # Creates a list of numbers [10, 20, 30, 40, 50]
    # Creates an iterator for the list
    # Uses a for loop with the iterator to print all elements

# 📌 Requirements:
    # Use iter()
    # Use for loop over the iterator

list2 = [10, 20, 30, 40, 50]
list2it = iter(list2)

for x in list2it:
    print(x)

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 📊 Task 3 — Iterator with Custom Stop Condition

# Write a program that:
    # Creates a list [5, 10, 15, 20, 25]
    # Creates an iterator for the list
    # Uses next() inside a while True loop
    # Stops printing when a number greater than 15 is encountered

# 📌 Requirements:
    # Use iter() and next()
    # Use try...except StopIteration to end the loop if needed


list3 = [5, 10, 15, 20, 25]
list3it = iter(list3)

while True:
    try:
        x = next(list3it)
        if x > 15:
            break
        print(x)
    except StopIteration:
        break

print("____________End of Ex 3")