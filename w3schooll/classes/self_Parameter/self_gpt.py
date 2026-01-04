# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧪 Task 1 — Using self to Access Attributes

# Task:
    # Create a class Person
    # Use __init__ to store name
    # Create a method say_hello() that prints:
    # Hello, my name is <name>

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}!")

p1 = Person("John")
p1.say_hello()


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — self in Multiple Methods

# Task:
    # Create a class Car
    # Store brand and year using self
    # Create:
        # get_brand() → prints the brand
        # get_year() → prints the year

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_brand(self):
        print(self.brand)

    def get_year(self):
        print(self.year)

    def get_all(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

car1 = Car("Toyota", 1999)
car1.get_all()


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 🧪 Task 3 — Modifying Object Data with self

# Task:
    # Create a class Counter
    # Store value (start from 0)
    # Create methods:
        # increase() → increases value by 1
        # show() → prints current value

class Counter:
    def __init__(self, value=0):
        self.value = value

    def increase(self):
        self.value += 1

    def show(self):
        print(self.value)

con = Counter()
con.increase()
con.show()

print("____________End of Ex 3")