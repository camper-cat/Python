# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# Task 1 — Read a Class Property

# Task:
    # Create a class Person
    # Add a property name using __init__
    # Create a method show_name() that prints the name

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

p1 = Person("Alex")
p1.show_name()


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# Task 2 — Modify a Class Property

# Task:
    # Create a class Car
    # Add a property speed
    # Create a method accelerate() that increases speed by 10
    # Create a method show_speed() that prints current speed

class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def show_speed(self):
        print(self.speed)

car1 = Car()
car1.accelerate()
car1.show_speed()

car1.accelerate()
car1.show_speed()


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Delete a Class Property

# Task:
    # Create a class Student
    # Add properties name and grade
    # Delete the grade property using del
    # Try to print grade after deletion (observe the result)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def show_grade(self):
        print(self.grade)

st1 = Student("Alex", 25)
st1.show_grade()

del st1.grade
st1.show_grade()


print("____________End of Ex 3")