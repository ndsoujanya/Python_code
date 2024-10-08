# method 1 , divide the given string into number max_width
import textwrap

# def wrap(string, max_width):
#     list1 = list(string)
#     print(list1)
#
#     list2 = []
#
#     count = 0
#     i=0
#
#
#     while i < len(list1):
#         result = ''
#         print(len(list1))
#         for x in range(0, max_width):
#             if i < len(list1):
#                 result += list1[i]
#                 i += 1
#             else:
#                 break
#         print(result)
#         list2.append(result)
#
#     return list2
#
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#
#     list2 = wrap(string, max_width)
#     for ls in list2:
#         print(ls)


# method 2: short method using textwrap

def wrap2(string,max_width):

    #TextWrapper function divide the given string into max_width
    # if given string is 20 letters it will divide it to 4 letter each
    wrapper = textwrap.TextWrapper(width=max_width)
    string = wrapper.fill(text=string)

    #print(string)

    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())

    list_new = wrap2(string, max_width)
    print(list_new)
