def mutate_string(string, position, character):

    x = [x for x in string] # list  comprehension converts given string to list
    x.insert(position, character)# insert element to given position
    print(x)
    x.pop(position+1)# delete element from position + 1
    print(x)
    y = "".join(x)
    return y

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)