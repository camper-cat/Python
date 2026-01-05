# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# Task 1 — Polymorphism with Different Classes

# Task:
    # Create a class Cat with a method make_sound() that prints "Meow"
    # Create a class Dog with a method make_sound() that prints "Bark"
    # Create objects of both classes and call make_sound()

class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Bark")

cat1 = Cat()
dog1 = Dog()

cat1.make_sound()
dog1.make_sound()

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# Task 2 — Polymorphism with Inheritance

# Task:
    # Create a parent class Animal with a method make_sound() that prints "Some sound"
    # Create child classes Cat and Dog that override make_sound()
    # Create objects of both classes and call make_sound()

class Animal:
    def make_sound(self):
        print("Some sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

animal1 = Animal()
cat1 = Cat()
dog1 = Dog()

animal1.make_sound()
cat1.make_sound()
dog1.make_sound()



print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Polymorphism in a Loop

# Task:
    # Create classes Car and Bike
    # Both classes must have a method move()
    # Put objects of both classes into a list
    # Use a for loop to call move() for each object

class Car:
    def move(self):
        print("The car is driving")


class Bike:
    def move(self):
        print("The bike is going")

car1 = Car()
bike1 = Bike()

vehicle = [car1, bike1]

for x in vehicle:
    x.move()

print("____________End of Ex 3")