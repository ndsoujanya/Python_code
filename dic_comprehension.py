# example of dictionary comprehension
# read a list and create a dictionary of name and its length
names = ['Soujanya' , 'Abhinandan' , 'Shahsikala']

d = {name : len(name) for name in names}

print(d)

# create new dictionary with city name where population is greater than 10

city_population ={
    'Mysore' : 30,
    'Bangalore' : 50,
    'Mandya' : 10,
    'Kundapura' : 5

}

dl = {key : value for key,value in city_population.items() if value > 10}
print(dl)

# how to convert sentence to a list

greeting = "Happy new year"

# split function reads any input and create list of elements based on delimiter
l = greeting.split() # default delimiter is space

print(l)

# how to read list of integer using split function

i = list(map(int,input("Enter list of numbers ").split()))

print(i)

# how to create list using '-' delimiter

string = "happy-new-year"

lt = string.split('-')

print(lt)

# covert integer string to actual integer list

lt = input("Enter list of integer ").split()

x = [int(num) for num in lt]

print(x)