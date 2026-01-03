thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist += ["apple"]
print(thislist)
print(len(thislist))

print()

mylist = ["apple", 34, True]

print(type(mylist))
print(type(mylist[0]))
print(type(mylist[1]))
print(type(mylist[2]))
print()


thislist = list(("apple", 34, True))
print(thislist)
print()


# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print()

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
print()

# Insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
print()

# Append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print()

# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print()

# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)
print(thislist)
print()

# Remove (.remove method removes 1st value(
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print()

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:
del thislist[0]
print(thislist)
print()

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print()

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print()

# there are a short hand for
[print(x) for x in thislist]
print()

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

print()

# List Comprehension
# Standart

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
print()

# The condition is optional and can be omitted:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]

print(newlist)
print()

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
print()

# Sort Lists

thislist = ["mango", "banana", "cherry", "apple", "kiwi"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
print()

# Copy Lists
# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.

# You can use the built-in List method copy() to copy a list.
list1 = ["apple", "banana", "cherry", "kiwi", "mango"]

list2 = list1.copy()
print(list2)

list3 = list(list1)
print(list3)

list4 = list1[:]
print(list4)
print()

# Join Lists
print("Join Lists")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Or

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# List methods

# Method	        Description
# append()	        Adds an element at the end of the list
# clear()	        Removes all the elements from the list
# copy()	        Returns a copy of the list
# count()	        Returns the number of elements with the specified value
# extend()	        Add the elements of a list (or any iterable), to the end of the current list
# index()	        Returns the index of the first element with the specified value
# insert()	        Adds an element at the specified position
# pop()	            Removes the element at the specified position
# remove()	        Removes the item with the specified value
# reverse()	        Reverses the order of the list
# sort()	        Sorts the list
