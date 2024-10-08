# write a program to print Fibonacci Sequence
prev_a = 0
prev_b = 0
for i in range(0,17):

    if i == 0:
        print(i)
        prev_a = i
    elif i == 1:
        print(i)
        prev_b = i
    elif i > 1:
        i = prev_a + prev_b
        print(i)
        prev_a = prev_b
        prev_b = i


