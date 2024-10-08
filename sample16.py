# Assignment 1
"""
Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.
"""

tup_item = (1,2,3,5,6)

#Try to modify one of the elements. What happens?
#tup_item[0] =3 # this line gives error because we cannot change tuple

#tup_item[0:3] # slicing does not works in tuple

#Perform slicing on the tuple to extract the second and third elements.
print(tup_item.index(1)) #get index of 2nd element from tuple
print(tup_item.index(2)) #get index of 3rd element from tuple

#Concatenate the tuple with another tuple.
# similar to string we can concatenate tuple using + sign
tuple2=(5,6,7,8)

final_tuple = tup_item + tuple2

print(final_tuple)







