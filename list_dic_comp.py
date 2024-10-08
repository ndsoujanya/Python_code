# assignments 1

# Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

list1 = ['dose', 'idlly', 'mude']

new_list = [i.upper() for i in list1]

print(new_list)

################################################

# assignments 2

# Create a dictionary of 5 items with their prices.
# Write a program that calculates the total price of all items using a for loop.

dict_1 = {
    'dose': 10,
    'idlly': 20,
    'chapati': 30
}

sum = 0
for key, value in dict_1.items():
    sum += value

print(f'sum of all items : {sum}')

##############################################

# assignment 3

# Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.

list_1 = [i for i in range(1,11)]

print(list_1)

list_2 = [i*i for i in list_1]

print(list_2)

###########################################################

# assignment 4

# Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student.
# Loop through the list and print each student's information.

dict_1 = {
    'name' : 'Souj',
    'age' : 27,
    'marks' : 100
}

dict_2 = {
    'name' : 'Abhi',
    'age' : 30,
    'marks' : 101
}

dict_3 = {
    'name' : 'Amma',
    'age' : 45,
    'marks' : 102
}

list5 = [dict_1,dict_2,dict_3]

for key , value in enumerate(list5):
    print(value)


############################################################

# assignment 5

# Create a dictionary where the keys are Kannada cities, and the values are their populations.
# Use dictionary comprehension to filter out cities with populations below 10 lakhs.

city_dict = {
    'mysore' : 1000000,
    'bangalore' : 2000000,
    'mandya' : 3000000
}

city_dict_2 = {key:value for key , value in city_dict.items() if int(value) > 1000000}
print(city_dict_2)

##################################
# assignment 6

# Write a Python program that takes a list of lists (a 2D list) as input and:
# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.

list_matrix = []

list_n = int(input("Enter number of rows"))
for i in range(list_n):
    x = list(map(int, input("Enter row by row").split()))
    list_matrix.append(x)

print(list_n)
print(list_matrix)


for matrix in list_matrix:
    #print(matrix)
    sum = 0
    for j in matrix:
        sum += j
    print(f'sum of {matrix}: {sum}')


