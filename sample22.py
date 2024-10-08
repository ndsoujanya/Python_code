# for loop
x=['apple','banana','pineapple']
for i in x:
    print(i)

for i in range(len(x)):
    print(x[i])

# print second number after each number 1 , (1+2) = 3, (3+2) = 5
for i in range(1,12,2):
    print(i)

print("===================")
# print or read in reverse order, use negative index
for i in range(12,0,-1):
    print(i)

# reverse a string using for loop
y = "apple"
z=""
# reads the string from last position and reads next element by -1, i.e. 5-1=4, 4-1=3 etc..
for i in range(len(y),0,-1):

    z+=y[i-1]
    print(z)
# perfect square

for i in range(1,501):
    print(i*i)
