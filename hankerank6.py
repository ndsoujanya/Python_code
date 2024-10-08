# use regular expression import re
import  re

lower = '[a-z]'
upper = '[A-Z]'
digit = [0-9]

def lower_upper(s):
    if re.search(lower, s):
        print(True)
    else:
        print(False)
    if re.search(upper, s):
        print(True)
    else:
        print(False)

if __name__ == '__main__':

    s = input()
    print(s.isalnum())
    if s.isalnum():
        print(True)
        print(True)
        print(True)
        lower_upper(s)
    else:
        print(False)

        if re.search(lower,s) or re.search(upper,s):
            print(True)
        else:
            print(False)

        if re.search(digit,s):
            print(True)
        else:
            print(False)

        lower_upper(s)




