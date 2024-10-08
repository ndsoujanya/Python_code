# examples on list Comprehension
# how to create new list using existing list
# with list Comprehension

ls = [1,3,5,7,9,33]

# perform i*2 for each list item and add it to new list-dl
dl = [i*2 for i in ls]

print(dl)

# create new list of square , 4 , 9 ,16 , 25....100

l_sqr = [item**2 for item in range(2,11)]
print(l_sqr)

# create new list of square , 4 , 16 ....100 only if it is even number
# if item%2 == 0 this condition true then only do square of a number

l_sqr_e = [item**2 for item in range(2,11) if item%2 == 0]
print(l_sqr_e)

# take only 2nd letter of given string of list and create new list
ls = ['souj' , 'abhi' , 'baby']

cl = [item[1] for item in ls]

print(cl)

