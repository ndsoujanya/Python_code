# more on strings

a = "Helloworld"
print(a[0])  # reads 1st character
print(a[9])  # reads last character
print(a[-1])  # reads last character using negative indexing
print(a[-10])  # reads 1st character

print(a[1:5])  # reads from 2nd character to 5th character
print(a[:])  # it prints all charters if 1st and last index is not specified
print(a[1:])  # reads from 1st index and ends at last index
print(a[:6])  # reads from 0th index to 5th index

print(a[1:6:2])  # reads from 1st index till 5th index and always skips 1 character and print next character
print(a[1:6:3])  # reads from 1st index till 5th index and always skips 2 character and print next character
print(a[1:6:1])  # reads from 1st index till 5th index and always skips 0 character and print next character
