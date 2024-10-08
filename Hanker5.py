def count_substring(string, sub_string):
    x = string.count(sub_string)
    sub_string_count = 0
    count=0
    while True:
        y_1 = string.index(sub_string)
        print(y_1)
        if y_1 > 1:
            sub_string_count +=1
            print("1",sub_string_count)
            ls = string.split()
            print("2",ls)
            #ls.count(sub_string)
            print("3",ls.count(sub_string))
            break



    return x


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print("4",count)