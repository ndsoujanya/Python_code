"""
String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
Prints how many characters are in the string, excluding spaces.
Write a program for escape charter demonstration
"""

str_inp = input("Enter a string ")

# Prints the sentence in all lowercase.
print(str_inp.lower())

# Prints the sentence in all uppercase.
print(str_inp.upper())

# count of characters in a given string including spaces
print("Number of characters (including spaces)", len(str_inp))


# count of characters in given string excluding spaces

num = len(str_inp) - str_inp.count(" ")

print("Number of characters (excluding spaces)", num)

# replace space with underscore(_)
print(str_inp.replace(' ','_'))

# Write a Python program that uses escape sequences to print the following output

print("This is back slash : \\")

# remove left / trailing spaces by default
print(str_inp.lstrip())

# remove right / leading spaces
print(str_inp.rstrip())

# remove both leading and trailing spaces
print(str_inp.strip())

# This method is used to delete all the leading characters mentioned in its argument.

print(str_inp.lstrip('-'))

# Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:

print('Hello\n    world\nthis is back slash: \\')

# Print hello world 10 times
a = "Hello world "

print(a*10)