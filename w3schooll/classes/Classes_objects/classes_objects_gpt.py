# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧪 Task 1 — Create a Simple Class

# Task:
    # Create a class called Person
    # Add a method greet() that prints "Hello!"
    # Create an object of the class and call the greet() method

class Person:
    def greet(self):
        print("Hello!")

p = Person()
p.greet()



print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — Add Attributes

# Task:
    # Create a class Person with attributes name and age
    # Create an __init__ method to set these attributes
    # Create an object with your own name and age
    # Print the name and age of the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alex", 27)
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 🧪 Task 3 — Class Method

# Task:
    # Create a class Rectangle with attributes width and height
    # Add a method area() that returns the area of the rectangle
    # Create an object of Rectangle and print the area

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 6)
print(rectangle.area())


print("____________End of Ex 3")