# use of hash function in python
t = tuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input("Enter number of element in the tuple"))
x= list()
z= list()
for i in range(n):
    x = tuple(map(int,input("Enter list of elements")))


    z.append(x)

print(z)
t = tuple(z)

print(t)

print(hash(t))

