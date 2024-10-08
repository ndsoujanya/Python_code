# Assignment on membership operators
"""Write a Python program that:

Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in)."""

str_inp = input("Enter a string")
if 'a' in str_inp:
    print(f"a is present in {str_inp}")

if "python" not in str_inp:
    print(f"{str_inp} is not in python")