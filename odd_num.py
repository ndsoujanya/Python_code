#Create a program that prints all odd numbers between 1 and 20 using a while loop.

n=1
while n <= 20:

    if n%2 !=0:
        print(f"{n} is odd number")
    else:
        print(f"{n} is even number")

    n += 1