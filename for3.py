# generate new list with double of given list

l = [1,5,8,10,44]

dl = []

for i in l:
    dl.append(i*2) # its doubling given list of elements

print(dl)

# loop through dictionary

student_marks = {'Anajali' : 10 , 'abhi':30 , 'baby' :40 }

# this will print key value only
for students in student_marks:
    print(students)

# loop through dictionary
for values in student_marks:
    print(f'{values}: {student_marks[values]}')

# How to fetch only key from dictionary
for keys in student_marks.keys():
    print(keys)

# How to fetch only values from dictionary
for values in student_marks.values():
    print(values)

# How to fetch both keys and values
for key, values in student_marks.items():
    print(f"{key}: {values}")


# take 2 list and convert it into one dictionary

students = ['abhi' , 'baby', 'shashi']

marks = [30,40,50]

students_marks = {}

for student in students:
    for mark in marks:
        students_marks[student] = mark


print(students_marks)

# 2nd method using enumerate to convert  list to  dictionary

for index, key in enumerate(students):

    students_marks[key] = marks[index]

print(students_marks)

# 3rd method using range function

for i in range(len(students)):
    students_marks[students[i]] = marks[i]

print(students_marks)

