# sets in python
# unordered
set_1 = {1,3,8,5}
print(set_1)

# unindexed
#print(set_1[0]) # it gives error cannot access set element using index

# it holds only unique elements
# as already '1' exits , even though we add '1' 2 times it consider it only once
set_1.add(1)

print(set_1)

# it gives all elements between 2 sets
set_2 = set_1.union([6,7,5])
print(set_2)

# gives common elements between 2 sets
print(set_1.intersection(set_2))

# gives un common elements between set-2 and set-1 sets
print(set_2.difference(set_1))