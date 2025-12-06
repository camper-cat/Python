my_dict = {
    'name': 'Alice',
    'age': 35,
    'city': 'New York'
}

print()
print("Original dictionary: ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()

my_dict['Profession'] = 'Doctor'
my_dict['age'] = 40

print("Updated dictionary after adding: ")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print()


print('City:', my_dict['city'])