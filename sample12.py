"""Nested List Challenge:
Write a Python program that takes a list of lists (a 2D list) as input and:

Prints the entire matrix row by row.
Prints the sum of each row in the matrix."""

# take number of rows of matrix to be created
row = int(input("Enter a number of rows"))

# intialize empty list
matrix = []

# loop 3 times and take 3 rows of input
for i in range(row):
    # map is used to convert each string input to integer and then append to matrix list
    mat = list(map(int,input(f"Enter {i+1} row").split()))
    matrix.append(mat)

# display the matrix
print(matrix)


# display the matrix row wise and display sum row wise
for i in range(row):
    sum_all = 0
    #print(matrix[i])
    for j in range(row):
        sum_all += matrix[i][j]

    print(sum_all)










