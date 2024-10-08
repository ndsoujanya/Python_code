

# how to use filter
"""In this example it applies the filter() function to a list of
numbers to extract only the even numbers, resulting in a list containing only
the even elements. Finally, it prints the list of even numbers.
"""


def is_even(n):
    return n % 2 == 0


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = filter(is_even, num)
even = list(even)
print(even)

# map function
"""In this example it applies the map() function to a list of
numbers to multiple by 2, resulting in each list of element multiple by 2.
"""
def is_double(n):
    return n*2
double = map(is_double,even)
double = list(double)
print(double)

#reduce is present in functools library
from functools import reduce

# reduce function
"""In this example it applies the reduce() function to a list of
numbers to calculate sum of list of element
"""
def sum_num(sum_n,n):
    return sum_n + n

sum_all = reduce(sum_num,double)
print(sum_all)


# split function converts the given string into list

item = input("Enter numbers ").split()
print(type(item))
print(item)

# how to convert list of string into integer list
#we can use map function to convert list of string to integer list
item = map(int,input("Enter numbers ").split())
item_ls = list(item)
print(type(item))
print(item_ls)




