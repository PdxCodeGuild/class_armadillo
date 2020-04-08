num = int(input("enter a number: "))
if num >= 90 and num < 100:
    if num % 10 > 5:
        print(num + "you got an A+")
    elif num % 10 < 5:
        print(num + "you got an A-")
elif num > 80 and num < 89:
    if num % 10 > 5:
        print("you got a B+")
    elif num % 10 < 5:
        print("you got a B-")
elif num > 70 and num < 79:
    if num % 10 > 5:
        print("you got a C+")
    elif num % 10 < 5:
        print("you got a C-")
elif num > 60 and num < 69:
    if num % 10 > 5:
        print("you got a D+")
    elif num % 10 < 5:
        print("you got a D-")
else:
    print("you failed. study next time")