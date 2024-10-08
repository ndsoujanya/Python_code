import re

low_pattern = '[a-z]'


def swap_case(s):
    new_s = ''
    for i in s:
        # search is used to find specific pattern
        # will check if the letter belongs to lower , if yes then convert to upper , else lower
        if re.search(low_pattern, i):
            x = i.upper()
            #print("1st if", x)
        else:
            x = i.lower()

        #print("second if", x)
        new_s += x

    return new_s


if __name__ == '__main__':
    s = input("Enter a string")
    result = swap_case(s)
    print(result)

    import re
