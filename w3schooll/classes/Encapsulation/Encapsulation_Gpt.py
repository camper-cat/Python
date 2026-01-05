# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# Task 1 — Public Attribute

# Task:
    # Create a class Person
    # Add a public attribute name
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

# Task 2 — Protected Attribute (_attribute)

# Task:
    # Create a class Account
    # Add a protected attribute _balance
    # Create a method show_balance() that prints the balance
# 📌 Note: _balance should still be accessible, but marked as internal.

class Account:
    def __init__(self, balance):
        self._balance = balance

    def show_balance(self):
        print(self._balance)

ac1 = Account(100)
ac1.show_balance()

print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# Task 3 — Private Attribute (__attribute)

# Task:
    # Create a class User
    # Add a private attribute __password
    # Create a method check_password() that prints the password
# 📌 Note: Access __password only inside the class.

class User:
    def __init__(self, password):
        self.__password = password

    def check_password(self):
        print(self.__password)

user1 = User("qwerty")
user1.check_password()

print("____________End of Ex 3")