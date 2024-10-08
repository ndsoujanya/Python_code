# tuples

# while creating single element in tuple if we don't use common
# then it will be considered as string
tup_itemes = ("apple")

print(tup_itemes)
print(type(tup_itemes))

# how to create single element in tuple
# its mandatory to add common after each element in tuple
# even when we create single element tuple
tup_itemes = ("apple",)
print(tup_itemes)
print(type(tup_itemes))

# methods used with tuples
# used to count how many times given element is present in tuple
print(tup_itemes.count("apple"))
# used to find index of given element is present in tuple
print(tup_itemes.index("apple"))
# used to find length of tuples
print(len(tup_itemes))

gender = ("male","female","others","male")
# index in tuple
print(gender[0])
print(gender[0:])
print(gender[:2])
# it gives index of first occurrence of given element
print(gender.index("male"))

# it gives number of occurrence/count of given element in tuple
print(gender.count("male"))
