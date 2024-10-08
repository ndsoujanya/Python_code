# Assignment on logical operators
"""
# Write a Python program that takes two numbers as input from the user and checks if:
Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).
"""

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if not (num1 > num2):
    print("The first number is not greater than the second")

if num1 > 5 or num2 > 5:
    print("at least one number is greater than 5")

if num1 > 10 and num2 > 10:
    print("Both numbers are greater than 10")
