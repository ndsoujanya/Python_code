#Assigment 3
"""Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?"""

list_item = [1,3,5,8,8,9,5]

# list is order and allow duplicates
# it allows to add/remove items
print(list_item)

# convert list to tuple , it is order and allow duplicate
# its does not allow to add/remove items
tup_item = tuple(list_item)

print(tup_item)

# convert list to set , it is unordered and does not allow duplicate
# it allow to add/remove items
set_item = set(list_item)

print(set_item)

# add new element to set
set_item.add("apple")

print(set_item)

# remove element from set
set_item.remove(8)

print(set_item)


