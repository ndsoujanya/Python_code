# assignment 1

# Create a dictionary to store information
# about 5 cities in Karnataka and their famous dishes.

cities = {
    'Mysuru' : 'Dosa',
    'Nanjangud' : 'Banana',
    'Dharwad' : 'Bene Dosa'
}

print(cities)
# Add a new city and its dish to the existing dictionary.

cities['Mandya'] = 'Ragi ball'

print(cities)

# Update the dish for Mysore.

cities['Mysuru'] = 'Malige Idly'

print(cities)

#Remove one city from the dictionary.

cities.pop('Nanjangud')

print(cities)

# Use the keys() method to print all city names in the dictionary.

print(cities.keys())

# Use the values() method to print all city names in the dictionary.
print(cities.values())

