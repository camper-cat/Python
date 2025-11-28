# Exercise 8: Generate a Python list of all the even numbers between 4 and 30

def list1():
    even_numbers = []
    for x in range(4, 30):
        if x % 2 == 0:
           even_numbers.append(x)
    print(even_numbers)

list1()

# or
def list2():
    even_numbers = [x for x in range(4, 30) if x % 2 == 0]
    print(even_numbers)

list2()

# or

def list3():
    print(list(range(4,30,2)))

list3()