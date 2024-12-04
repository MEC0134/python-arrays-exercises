"""Below you may find a few exercises with their solutions related to python lists """

# Exercise 1: Write a Python program to sum all the items in a list.

list1 = [7,3,8,12,3,9]

# Store total
x = 0

for i in list1:
    x += i

print("\nThe total of all values in the list is:", x, "\n")


# Exercise 2: Write a Python program to multiply all the items in a list.

# function to multiply list items

def multiply_items(list):

    result_list = []

    for i in list:
        x = i*2
        result_list.append(x)

    print(result_list)


multiply_items([2,4,6,8])
print("\n")


# Exercise 3: Write a Python program to get the largest number from a list.


def get_largest_num(list):

    max = list[0]

    for x in list:

        if x > max:
            max = x

    return max

print("The largest number in list is:", get_largest_num([3,5,1,7,-21]), "\n")



# Exercise 4: Write a Python program to get the smallest number from a list.

def get_smallest_num(list):

    min = list[0]

    for i in list:

        if i < min:

            min = i

    return min


print("The smallest number in the list is:", get_smallest_num([12, 3, 9, -2, 1, -12]), "\n")


"""

Exercise 5: 

Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

"""

# list_with_tups = [(1,2),(1,1),(2,12),(3,21),(9,19),(2,3)]
#
# def sort_list_with_tuples(list):
#
#     x = list[0][1]
#
#     for i,k in list:
#
#         print(i, k)





sort_list_with_tuples(list_with_tups)
