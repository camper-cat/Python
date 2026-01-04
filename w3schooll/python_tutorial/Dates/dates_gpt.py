# ============================= Start of Exercises

# ---------------------- Task 1
print("____________Start of Ex 1")

# 🧠 Task 1 — Current Date and Time

# Write a program that:
    # Imports the datetime module
    # Prints the current date and time

# 📌 Requirements:
    # Use datetime.datetime.now()
    # Print directly

import datetime

current_time = datetime.datetime.now()
print(current_time)


print("____________End of Ex 1")
print()
# ----------------------- The end of Ex 1


# ------------------------- Start of Ex 2
print("____________Start of Ex 2")

# 🔢 Task 2 — Extract Year, Month, Day

# Write a program that:
    # Imports the datetime module
    # Gets the current date
    # Prints the year, month, and day separately

# 📌 Requirements:
    # Use .year, .month, .day attributes

current_date = datetime.datetime.now()
print(f"Year: {current_date.year}")
print(f"Month: {current_date.month}")
print(f"Day :{current_date.day}")


print("____________End of Ex 2")
print()

# --------------------- End of Ex 2

# ---------------------- Start of Ex 3
print("____________Start of Ex 3")

# 📊 Task 3 — Format the Date

# Write a program that:
    # Imports the datetime module
    # Gets the current date
    # Prints it in the format DD-MM-YYYY

# 📌 Requirements:
    # Use strftime("%d-%m-%Y")

current_date2 = datetime.datetime.now()

print(current_date2.strftime("%d-%m-%Y"))

print("____________End of Ex 3")