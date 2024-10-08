# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# in given dictionary find the average of given student marks

# The average of the marks obtained by the particular student correct to 2 decimal places.
if __name__ == '__main__':
    n = int(input("Enter number of students "))
    student_marks = {}
    scores = []
    for _ in range(n):
        name, *line = input("Enter name of students and 3 marks ").split()
        # print(name)
        # print(line)
        scores = list(map(float, line))  # marks read as string is converted into integer list
        # print(scores)
        student_marks[name] = scores # add the scores to dictionary based on names
        # print(student_marks)

    query_name = input("Enter for which student marks to be displayed")

    sum_n = 0
    avg_n = 0

    for i in student_marks:
        # print(i)

        if query_name == i:
            stu_score = student_marks[i]
            for j in stu_score:
                sum_n += j

    avg_n = sum_n / 3
    print(avg_n)
    print("%.2f" % avg_n)
