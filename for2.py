# multiplication of 3

for i in range(1,11):
    x = 3 * i
    print(f"3 * {i}=", x)

#Sum of First 10 Numbers:

sum_n = 0
for i in range(1,11):

    sum_n +=i

print(sum_n)

#Write a program that takes your name as input and
# prints each letter of your name using a for loop.

name = input("Enter your name ")

for i in name:

    print(i)

# Write a program that counts how many vowels are in a given string using a for loop.

string = input("Enter a string ")

vowels = ['a','e','i','o','u']

count = 0

for i in string:

    if i in vowels:

        count += 1

print(f"Count of Vowels in given string {count}")

# for loops with else
#  will be printed only when for loop completed successfully
# if for breaks in between for certain condition then else part won't execute

for i in range(1,10):
    print(i)
else:
    print("for completed")


# for start , stop , step
# setp =3 , 3 + 3 = 6 , 6 +3 = 9 , 9+3 = 12 etc..
for i in range(3,20,3):

    print(i)