# ======================= 1st way

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3 = []

def list_(list1, list2):
    for x in list1:
        if x % 2 != 0:
            list3.append(x)
    for y in list2:
        if y % 2 == 0:
            list3.append(y)



list_(list1, list2)
print(list3)

# 2d way

def func(list1, list2):
    list4 = [x for x in list1 if x % 2 != 0]
    list5 = [y for y in list2 if y % 2 == 0]
    return list4 + list5


print(func(list1, list2))
# 3d way

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def filter_list(list1, list2):
    odd_list = list(filter(lambda x: x % 2 != 0, list1))
    even_list = list(filter(lambda y: y % 2 == 0, list2))
    return odd_list + even_list

print(filter_list(list1, list2))


#

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda a: a > 5, list1))
print(new_list)

scnd_list = [x for x in list1 if x > 5]
print(scnd_list)

#

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x

new_arr = list(map(func, numbers))
print(new_arr)

#

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 768]
new_arr = list(map(lambda x: x, numbers))
print(new_arr)

#
