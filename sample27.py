# if elif else

n = int(input("Enter a number "))

if n % 2 ==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")


# if elif else

signal = input("Enter a color ")

if signal == "red":
    print("stop")
elif signal == "yellow":
    print("ready")
else:
    print("Go")

# nested if

gender = input("Enter gender ")
age = int(input("Enter the age"))

if gender == "female":
    print("ticket is free")
else:
    if age < 5:
        print("ticket is half price")
    elif age >= 60:
        print("ticket having senior citizens discount")
    else:
        print("pay full price")