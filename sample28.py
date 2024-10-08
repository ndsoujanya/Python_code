# Assignment 2
# Create a program that checks the time of day (24-hour format)
# and prints whether it's time for breakfast, lunch, or dinner.
# Breakfast: 8 AM
# Lunch: 1 PM
# Dinner: 8 PM
# If none of these times, print "It's not meal time."
time = int(input("Enter the current time "))
if time == 8:
    print("It's time for break fast")
elif time == 13:
    print("It's time for lunch")
elif time == 20:
    print("It's time for dinner")
else:
    print("It's not meal time.")