# Illustration of tuple immutability
names_tuple = ("Raj", "John", "Jabby", "Raja")

# Below attempt to update tuple will throw TypeError
# names_tuple[2] = "Enes"

#Illustration of list mutability
numbers_list = [1,2,3,4,5]


# append() - built-in method for lists, will add to end of list and only one at a time
numbers_list.append(6)


for i in range(7, 9):
    numbers_list.append(i)


# extend() - used to add multiple items at once to the end of the list
numbers_list.extend([9,10,11])

# insert() - add element in a given position, we can also loop to add multiple elements

for i in range(8, 13):
    numbers_list.insert(i, i+1)


# remove() - removes element from list, will remove 1st occurrence


# pop() - removes elements from any position in the list
numbers_list.pop(-1)


# slicing - used to print subset of list, we can specify star and end positions or not, colon : is a must,
# we can use to reverse list as well without affecting original list
# print(numbers_list[::-1])


# reverse() - reverses original list (Warning: will affect original list) syntax: list.reverse()


# min() - return smallest value from list, list must be homogenous
# print(min([2,4,1,6]))

# max() - return highest value from list, list must be homogenous
# print(max([2,4,1,6]))


# count(element) - returns number of occurrences of a specified element
# print(numbers_list.count(9))

# we can multiply a list
# numList = [1,2,3,4,5,6,7,8,9]
# print(numList*2)


# sort() - will sort list in ascending order
# numList = [4, 2, 6, 5, 0, 1]
# numList.sort()
# print(numList)


# clear() - clears list without deleting it



"""Tuple Built-in Methods"""

# len() - It returns the length of the tuple

myTuple = [1,2,3,4,5,6,7,8,9]
# print(len(myTuple))


# del - Tuples are immutable, but we can delete tuple using del tuple_name syntax

Tuple1 = (1, 3, 4, 'test', 'red')
del Tuple1


# Membership check with Tuple using in keyword
print(1 in myTuple, "\n")


# Getting the size in bytes of a list or tuple using __sizeof__()
a= (1,2,3,4,5,6,7,8,9,0)

b= [1,2,3,4,5,6,7,8,9,0]

print('a=',a.__sizeof__())

print('b=',b.__sizeof__())

a=104
b=120

"""

Different Use Cases
Python's lists are best suited to store data in the following situations: 

Several data types can be stored in lists, and their index can be used to access them.
Lists are good for mathematical operations on a group of elements because Python allows you to perform these operations directly on the list. 
If you don't know how many elements will be stored in your list ahead of time, it's easy to increase or decrease its size as needed.

Python's tuples are best suited to store data in the following situations: 

It’s best to use a tuple when you know the exact information that will go into the object's fields. 
For example, a tuple is okay for storing website credentials. 
The tuples are immutable (unchangeable), so they can only be used as keys for dictionaries. But if you want to use a list as a key, make it into a tuple first.

"""

# Using tuples as keys of dictionaries

tuplekey = {}

tuplekey[('blue', 'sky')] = 'Good'

tuplekey[('red','blood')] = 'Bad'

# print(tuplekey)


# Tuple Packing and Unpacking - Packing & unpacking improves code readability. Packing is assigning multiple values to tuple.
# Unpacking is assigning values to individual variables.

# Tuple Packing
person = ("Enes", "6 ft", "Employees")

# Tuple Un-packing
(name, height, profession) = person

print("The persons name from our tuple is:", name, "and he is", height)
