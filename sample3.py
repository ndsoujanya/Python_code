# single-line comments
# 3 different ways to take input and print Ram loves sita
boy_name = input("Enter boy name: ")

# input function always returns string , so while working with number
# convert it to integer before using number in python
boy_age = int(input("Enter boy's age: "))
girl_name = input("Enter girl name: ")
girl_age = int(input("Enter girl age: "))

print(boy_name, "loves", girl_name)

# string concatenation using + sign
print(boy_name + " loves " + girl_name)



# using formatted string / f string

print(f"{boy_name} loves {girl_name}")

# multi-line comments
''' age difference between boy and girl
abs function is used to print -ve value to positive '''

print(f"Age difference between {boy_name} and {girl_name} is {abs(boy_age - girl_age)} ")


