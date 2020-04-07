#Lab 3: Grading

check_grading = True
while check_grading == True:
    print("Check grading ")
    

    num = int(input("Enter a number: "))

    if num >= 90:
        print(f"{num} you got an A great job!")
    elif num >= 80:
        print(f"{num} you got a solid B ")
    elif num >= 70:
        print(f"{num} you got an C")
    elif num >= 60:
        print(f"{num} you got an D")

    else:
        print(f"{num} you got an F")
    # check_grading = False
    
    while True:
        try_again = input('would you like to try again? yes/no')
        if try_again == "yes":
            break
        elif try_again == "no":
            check_grading = False
            break
        else:
            print("This is not a valid choice")
            continue


#while not num.isnumeric():
#    print("That's not a number. ")




# grade = input('enter your grade: ')
# if not grade.isnumeric():
#   print('is numeric')
# else:
#   print('is not numeric')
# ​
# # grade = 87
# print(grade // 10) # tens digit
# print(grade % 10) # ones digit