import json

# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧠 Task 1 — Convert Python Dictionary to JSON

# Write a program that:
 # Imports the json module
 # Creates a Python dictionary, e.g.:
    # person = {"name": "Alice", "age": 25, "city": "Kyiv"}
 # Converts the dictionary to a JSON string using json.dumps()
 # Prints the JSON string

person = {
    "name": "Alice",
    "age": 25,
    "city": "Kyiv"
}

personjson = json.dumps(person, indent = 4)

print(personjson)

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🔢 Task 2 — Convert JSON String to Python Dictionary

# Write a program that:
    # Imports the json module
    # Uses the JSON string:
        # json_str = '{"name": "Bob", "age": 30, "city": "Lviv"}'
    # Converts it to a Python dictionary using json.loads()
    # Prints the dictionary

json_str = '{"name": "Bob", "age": 30, "city": "Lviv"}'

python_str = json.loads(json_str)

print(python_str)



print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 📊 Task 3 — Read JSON from User Input

# Write a program that:
    # Imports the json module
    # Asks the user to input a JSON string representing a person, e.g.:
        # {"name": "Carol", "age": 28, "city": "Odessa"}
    # Converts it to a Python dictionary
    # Prints each key and value on a separate line

json_input = input("Enter JSON string: ")

try:
    python_converted = json.loads(json_input)
    for key, value in python_converted.items():
        print(f"{key}: {value}")
except json.JSONDecodeError:
    print("Invalid JSON! Please check the format.")


print("____________End of Ex 3")