import re
# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧠 Task 1 — Find All Digits in a String

# Write a program that:
    # Imports the re module
    # Takes a string from the user
    # Finds all digits in the string
    # Prints them as a list

# 📌 Requirements:
    # Use re.findall()
    # Pattern should match digits

string1 = input("Enter a string: ")

x = re.findall(r"\d", string1)
print(x)

print("____________End of Ex 1")
print()

# ----------------------- The end of Ex 1




# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🔢 Task 2 — Check if a String Starts with a Specific Word

# Write a program that:
    # Imports the re module
    # Takes a string from the user
    # Checks whether the string starts with the word "Hello"
    # Prints True or False

# 📌 Requirements:
    # Use re.search() or re.match()
    # Use a regular expression pattern

string2 = input("Enter a string: ")

y = re.search(r"^Hello", string2)
print(bool(y))


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 📌 Task 3 — Find All Email Addresses (RegEx)

# Task:

# Write a program that:
    # Imports the re module
    # Asks the user to enter a string
    # Finds all email addresses in the string
    # Prints the found email addresses as a list

email = input("Enter your email: ")

pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, email)

print(emails)

print("____________End of Ex 3")