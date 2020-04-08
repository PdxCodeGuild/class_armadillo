while True:
    num_grade = input("Enter a number grade: ")
    if num_grade.isnumeric():
        num_grade = int(num_grade)
        break
    print('Invalid...is not numeric.')

sign_grade = num_grade % 10
sign = ' '

if sign_grade > 5:
    sign = '+'
elif sign_grade < 5:
    sign = '-'

if num_grade >= 90:
    print('Letter grade: A' + sign)
elif num_grade >= 80:
    print('Letter grade: B' + sign)
elif num_grade >= 70:
    print('Letter grade: C' + sign)
elif num_grade >= 60:
    print('Letter grade: D' + sign)
else: 
    print('Letter grade: F' + sign)

 



