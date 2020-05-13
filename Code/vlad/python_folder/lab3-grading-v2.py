#Lab 3: Grading version 2
def get_grade(num):
    if num >= 90:
        grade = 'A' 
    elif num >= 80:
        grade = 'B'
    elif num >= 70:
        grade = 'C'
    elif num >= 60:
        grade = 'D'

    else:
        grade = 'F'

    qualifier = ''
    if num % 10 > 5:
        qualifier = '+' # to set another string to '+', '-', or ' '
    else:
        qualifier = '-'
    
    return f'{grade}{qualifier}'

check_grading = True
while check_grading == True:
    print("Check grading ")
    

    num = int(input("Enter a number: "))
    grade = get_grade(num)
    print(f'Your grade is {grade}')

   
    # check_grading = False
    
    while True:
        try_again = input('would you like to try again? yes/no: ')
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




#while True: 
    #grade = input('enter your number grade: ')
    #is grade.isnumeric():
      #grade = int(grade)
        #break
        #print('that is not a valid number')
#ones_digit = grade % 10
#tens_digit
# grade = input('enter your grade: ')
# if not grade.isnumeric():
#   print('is numeric')
# else:
#   print('is not numeric')
# ​
# # grade = 87
# print(grade // 10) # tens digit
# print(grade % 10) # ones digit