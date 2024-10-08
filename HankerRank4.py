# program to find second-lowest marks student names and order in ascending order
# https://www.hackerrank.com/challenges/nested-list/problem
list_stu = []
grade = []
if __name__ == '__main__':
    for _ in range(int(input("Enter number of elements "))):
        name = input("Enter names ")
        score = float(input("Enter scores "))
        list_stu.append([name, score])  # list of name and score
        grade.append(score)  # this list can be used to find 2nd lowest grade

    # print("List of student and grade ",list_stu)
    # print("list of grade ",grade)

    a = set(grade)  # this returns unique element as it is a set
    # print(a)
    a = list(a)  # convert set to list
    a.sort()  # now apply sort , which sorts in ascending order, lowest to highest

    # print(a[1]) # now print 2nd lowest element from the list

    second_lowest = a[1]

    # now we got 2d lowest marks
    # check which student matches that 2nd lowest marks

    stu_name = []  # list to get 2nd lowest marks student name
    for i in range(len(list_stu)):
        j = 1
        k = 0

        if second_lowest == list_stu[i][j]:
            stu_name.append(list_stu[i][k])
            #print(list_stu[i][j])
            #print(list_stu[i][k])

print("student names of second lowest marks students", stu_name)

stu_name.sort()  # sorted the given names

for i in stu_name:  # now iterate to print sorted names
    print(i)
