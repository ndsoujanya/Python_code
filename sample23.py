# break

for i in range(10):
    if i ==3: # if 'i' is 3 exit from loop
        break
    print(i)
print("=======================")
# continue
for i in range(10):
    if i ==3: # if 'i' is 3 skip this iteration and continue with 4(next iteration)
        continue
    print(i)
print("=======================")
# pass
n = int(input("Enter a number to check if its odd "))

if n%2 != 0:
    print("old number")
else:
    pass# if old print a message else dont print anything

