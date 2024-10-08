# Looping Through a List with enumerate()
# The enumerate() function allows you to loop over a sequence and
# get both the index and the value of each item.

# enumerate is used when we want both index and value details in given list
fruits = ['Apple', 'Banana' , 'Grape']
for index , value in enumerate(fruits):
    print(f'{value} at {index} index you can sell ')