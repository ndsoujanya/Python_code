def split_and_join(line):
    # write your code here

    x = line.split() # covert string into list
    #print(x)
    x = "-".join(x) # joins given list of string with hyphen
    #print(x)

    return x


if __name__ == '__main__':
    line = input("Enter a string")
    print(line)
    result = split_and_join(line)
    print(result)