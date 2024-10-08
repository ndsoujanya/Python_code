# for else

# for i in range(0,10):
#     if (i%2)==0:
#         print(i)
# else: # else always gets executed after for loop completion only
#     print("for completed successfully")

# else block does not execute when loop get terminated in middle without completing all iteration

for i in range(1,11):
    if (i%10)==0:
        break
    print(i)
else: # else always gets executed after for loop completion only
    print("for completed successfully")