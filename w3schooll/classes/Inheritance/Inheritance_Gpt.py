# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# Task 1 — Simple Inheritance

# Task:
    # Create a parent class Animal
    # Add a method make_sound() that prints "Some sound"
    # Create a child class Dog that inherits from Animal
    # Create an object of Dog and call make_sound()

class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    pass

Dog1 = Dog()
Dog1.make_sound()

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# Task 2 — Inheritance with __init__

# Task:
    # Create a parent class Person with name
    # Create a child class Student that inherits from Person
    # Use super() to pass name to the parent class
    # Add a method show_name() that prints the name

class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

p1 = Student("Alex")
p1.show_name()


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Add New Method in Child Class

# Task:
    # Create a parent class Vehicle with a method move() that prints "The vehicle moves"
    # Create a child class Car that inherits from Vehicle
    # Add a new method drive() that prints "The car is driving"
    # Create an object of Car and call both methods

class Vehicle:
    def move(self):
        print("The vehicle moves")


class Car(Vehicle):
    def drive(self):
        print("The car is driving")

car1 = Car()
car1.move()
car1.drive()


print("____________End of Ex 3")