my_dict = {
    'name': 'Alice',
    'age': 35,
    'city': 'New York',
    'profession': 'Doctor'
}

print()
print("Original dictionary: ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()

my_dict.pop('profession')

print("Dictionary after pop('profession'): ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()

print("Printing all key-value pairs: ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()


#
if "age" in my_dict:
    print(f"The key 'age' is in the dictionary.")
else:
    print(f"The key 'age' is not in the dictionary.")

#
print("age" in my_dict)