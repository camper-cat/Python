# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# Task 1 — Simple Inner Class

# Task:
    # Create a class Car
    # Inside Car, create a class Engine
    # Add a method start() in Engine that prints "Engine started"
    # Create a Car object and an Engine object inside it, then call start()

class Car:
    class Engine:
        def start(self):
            print("Engine started")

car1 = Car()
eng1 = car1.Engine()
eng1.start()


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# Task 2 — Access Outer Class Attribute

# Task:
    # Create a class Person with an attribute name
    # Inside it, create a class Address with a method show()
    # show() should print: "Name: {name}, Address: {some_address}"
    # Use a reference to the outer class object

class Person:
    def __init__(self, name):
        self.name = name

    class Address:
        def __init__(self, outer, some_address):
            self.outer = outer
            self.some_address = some_address
        def show(self):
            print(f"Name: {self.outer.name}, Address: {self.some_address}")

person1 = Person("Alex")
person_info = person1.Address(person1, "Lviv")
person_info.show()

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Inner Class with Constructor

# Task:
    # Create a class School with an attribute school_name
    # Inside it, create a class Student with an attribute student_name
    # Add a method show_info() that prints: "Student {student_name} studies at {school_name}"
    # Create a School object and a Student object inside it, then call show_info()

class School:
    def __init__(self, school_name):
        self.school_name = school_name

    class Student:
        def __init__(self, outer, student_name):
            self.outer = outer
            self.student_name = student_name

        def show_info(self):
            print(f"Student {self.student_name} studies at {self.outer.school_name}")


my_school = School("School_1")
student1 = my_school.Student(my_school, "Alex")
student1.show_info()


print("____________End of Ex 3")