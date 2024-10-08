# Lists in python
# empty list
item = list()
print(item)

# list with items
item = [10,10,10,1,"apple", [1,2,3]] # list holds different data type data and list holds another list

print(item) # print list items
print(item[2]) # print 2nd index element
print(item[-1]) # print last element in list

# add 10 at the end of list
item.append(10)
print(item)

# remove "apple" from list
item.remove("apple")
print(item)

# insert 30 at index 1 in list
item.insert(1,30)
print(item)

# pop index of 1 element from list
item.pop(1)
print(item)

# pop last element if no index specified
item.pop()
print(item)

# extends help to add multiple elements inside list and not single element
item.extend([8,9,10])
print(item)


# it replaces 3rd index element with new element banana
item[3] = "banana"
print(item)

# prints 0th index to 2nd index list element
print(item[:2])

# prints 0th index to 4th index list element
print(item[0:4])

# prints 0th index to 5th index list element, but skips every 2nd element
print(item[0:5:2])

# prints last element in list
print(item[-1])

# prints reverse of the list/same applies to string
print(item[::-1])

# print length of list
print(len(item))

# print count of given element in list (10 appears 4 times)
print(item.count(10))

# sorts the elements in ascending order
a = ['a','x','d','z','r']
print(sorted(a)) # here sort does not work between string and number

# sum of list elements
b = [1,8,10,12]

print(sum(b))

# index of given element in list
b = [1,8,10,12]

print(b.index(8))

# to delete all list element
item.clear()
print(item)


# 2 * 2 (2 D) matrix using list

matrix = [[1,2],[2,2],[3,4]]

print(matrix[0])

print(matrix[0][0]) # prints first element in 2D- list
print(matrix[0][1]) # prints 2nd element in 2D- list
print(matrix[1][0]) # prints 3rd element in 2D- list
print(matrix[1][1]) # prints 4th element in 2D- list
print(matrix[2][0]) # prints 5th element in 2D- list
print(matrix[2][1]) # prints 6th element in 2D- list


