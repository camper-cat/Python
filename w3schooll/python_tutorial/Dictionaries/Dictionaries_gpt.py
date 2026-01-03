# ====================== Start of Exercises

# --------------------- Start of Ex 1

print("___________Start of Ex 1")
print()
# Exercise 1: Dictionary Basics

# Goal: Practice creating and accessing dictionary values

# Instructions:
 # 1) Create a dictionary person with the following keys and values:
    # "name" → "John"
    # "age" → 25
    # "city" → "London"
 # 2) Print the value of the "name" key.
 # 3) Print the value of the "city" key.
 # 4) Change "age" to 30 and print the updated dictionary.

person = {
    "name": "John",
    "age": 25,
    "city": "London"
}

print(person["name"])
print(person["city"])
person["age"] = 30
print(person["age"])
print()


for key, value in person.items():
    print(f"{key}: {value}")

print()
print("_________End of Ex 1")
print()

# ------------------------- The End of Ex 1

# ------------------------- Start of Ex 2

print("_________Start of Ex 2")
print()

# Exercise 2: Adding and Removing Items

# Goal: Practice modifying dictionaries

# Instructions:
 # 1) Create a dictionary car with keys:
    # "brand": "Toyota"
    # "year": 2015
 # 2 Add a new key "color" with the value "red".
 # 3) Remove the "year" key using pop().
 # 4) Print the dictionary after each modification.

car = {
    "brand": "Toyota",
    "year": 2015
}

car["color"] = "Red"
car.pop("year")

for key, value in car.items():
    print(f"{key}: {value}")

print()
print("_________End of Ex 2")
print()

# ------------------ The End of Ex 2

# -------------------- Start of Ex 3

print("_________Start of Ex 3")
print()

# Exercise 3: Loops and Dictionary Methods

# Goal: Practice iterating through dictionaries and using dictionary methods

# Instructions:
 # 1) Create a dictionary scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
 # 2) Loop through the dictionary and print each key and its value in the format:
    # Alice: 85
    # Bob: 92
    # ...
# 3) Check if "Bob" exists in the dictionary using the in operator.
# 4) Use .keys(), .values(), and .items() and print each result.

scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

for key, value in scores.items():
    print(f"{key}: {value}")

if "Bob" in scores:
    print(f"Yes, {"Bob"}, is in scores")

print()

keys = scores.keys()
print(keys)
values = scores.values()
print(values)
items = scores.items()
print(items)
