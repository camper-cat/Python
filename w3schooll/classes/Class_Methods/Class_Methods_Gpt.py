# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# Task 1 — Simple Class Method

# Task:
    # Create a class Person
    # Add a method greet() that prints "Hello!"
    # Create an object and call greet()

class Person:
    def greet(self):
        print("Hello!")

p1 = Person()
p1.greet()

print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🧪 Task 2 — Class Method with Attributes

# Task:
    # Create a class Car with attributes brand and year
    # Add a method show_info() that prints: "Brand: <brand>, Year: <year>"
    # Create an object and call show_info()

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

car1 = Car("Ford", "2008")
car1.show_info()


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Update Object Data with a Method

# Task:
    # Create a class Counter with attribute value (default 0)
    # Add a method increase() that adds 1 to value
    # Add a method show() that prints the current value
    # Create an object, call increase() multiple times, and then show()

class Counter:
    def __init__(self, value=0):
        self.value = value
    def increase(self):
        self.value += 1
    def show(self):
        print(self.value)

con1 = Counter(0)
con1.increase()
con1.increase()
con1.increase()
con1.show()


print("____________End of Ex 3")