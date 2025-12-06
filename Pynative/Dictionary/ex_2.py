my_dict = {
    'name': 'Alice',
    'age': 35,
    'city': 'New York',
    'profession': 'Doctor'
}

# Output original dict
print()
print("Original dictionary: ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()

# .pop()
my_dict.pop('profession')

print("Dictionary after pop('profession'): ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()

# Output all key-value
print("Printing all key-value pairs: ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()


# If 'key' in dict
if "age" in my_dict:
    print(f"The key 'age' is in the dictionary.")
else:
    print(f"The key 'age' is not in the dictionary.")

#
print("age" in my_dict)