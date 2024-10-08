# assignment 2

"""
Set Operations:
Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
"""

fruits_1 = {"Apple","Banana"}
fruits_2 = {"Mango","pineapple","Banana"}

# union of 2 sets, will all elements in both set without duplicates

print(fruits_1.union(fruits_2))


# intersection of 2 sets, will return only common elements from both set

print(fruits_1.intersection(fruits_2))

# difference of 2 sets, will return elements from 1st set and no elements from 2nd set(including common elements)
print(fruits_1.difference(fruits_2))

# add new element
fruits_2.add("Grape")
print(fruits_2)

# remove element using remove func
fruits_2.remove("Banana")
print(fruits_2)

# remove element using discard func
# this function does not give error even if element does not exist in set
# but remove func will give error if element does not exits
fruits_2.discard("Banana")
print(fruits_2)





