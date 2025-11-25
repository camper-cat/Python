# Write a program to create a function show_employee() with the following specifications:

# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000.


def show_employee(name = "Starting salary for everyone:", salary = 9000):
    return name, salary

print(show_employee())
print(show_employee("Alex"))

# with updating in name

# ============ Another way

def show_employee(name = "Starting salary for everyone:", salary = 9000):
    print(f"Name: {name}, Salary: {salary}")

show_employee("Alex", 1200)