# Assignment 3
# Write a program that checks whether a person is eligible for a library membership.
# If they are under 18, they get a student membership.
# If they are 60 or older, they get a senior citizen membership. Otherwise,
# they get a regular membership.

age = int(input("Enter a age for library membership "))

if age < 18:
    print("You will get student library membership")
elif age >= 60:
    print("You will ge senior citizen library membership")
else:
    print("You will ge regular library membership")