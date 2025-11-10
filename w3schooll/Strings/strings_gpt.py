# ============================== Start of Exercises ==================

# ------------------------------ Start of Exercise 1 -----------------
# 🧩 Task 1: Indexing and Slicing

# text = "Python is fun"

# 1. Print the first and the last character.
# 2. Print the first 6 characters.
# 3. Check if the word "fun" is in the string and print the result (True/False).

print("____________Ex 1")

text = "Python is fun"
print(text[0], text[-1])        # print 1st and the last character
print(text[:6])                 # print the first 6 characters
print("fun" in text)            # check if the word "fun" is in the string and print the result (True/False).
print()

# ------------------------------ End of Exercise 1 -----------------


# ----------------------------- Start of Exercise 2 -----------------

# 🧩 Task 2: String Methods
# msg = "   Hello, Python Learner!   "

# 1. Remove extra spaces.
# 2. Replace "Learner" with "Developer".
# 3. Convert all letters to uppercase.

print("____________Ex 2")

msg = "   Hello, Python Learner!   "
print(msg.strip())
print(msg.replace("Learner", "Developer").strip())
print(msg.upper().strip())
print()

# ------------------------------ End of Exercise 2 -----------------

# ----------------------------- Start of Exercise 3 -----------------

# 🧩 Task 3: String Formatting
# name = "Alex"
# age = 30


# 1. Print the sentence using an f-string:
# My name is Alex and I am 30 years old.
# 2. Print the same sentence using the format() method.

print("____________Ex 3")

name = "Alex"
age = 30

print(f"My name is {name} I am {age}, years old")       # f-string format
print("My name is {} I am {} years old.".format(name, age))

# ------------------------------ End of Exercise 3 -----------------

# ============================== End of Exercises ==================