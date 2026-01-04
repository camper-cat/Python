# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧪 Task 1 — Simple Initialization

# Task:
    # Create a class Person
    # Add an __init__ method that takes name as a parameter and assigns it to an attribute
    # Create an object of Person and print the name

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alex")
print(p1.name)


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — Multiple Attributes

# Task:
    # Create a class Car
    # Add an __init__ method that takes make, model, and year
    # Create an object of Car and print all attributes in a formatted string

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", "2020")
print(f"{car1.make} {car1.model}, {car1.year}")


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 🧪 Task 3 — Default Values

# Task:
    # Create a class Book
    # Add an __init__ method with parameters title, author, and pages
    # Give default values for author as "Unknown" and pages as 0
    # Create an object providing only the title
    # Print all attributes

class Book:
    def __init__(self, title, author="Unknown", pages=0):
        self.title = title
        self.author = author
        self.pages = pages

ob = Book("Mein Kampf")
print(f"Title: {ob.title}, Author: {ob.author}, Pages: {ob.pages}")



print("____________End of Ex 3")