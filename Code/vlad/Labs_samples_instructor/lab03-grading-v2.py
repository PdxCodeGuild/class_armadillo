#lab03-grading-v2 sample by instructor: 

while True:
    grade = input('enter your number grade: ')
    if grade.isnumeric():
        grade = int(grade)
        break
    print('that is not a valid number')

ones_digit = grade % 10
tens_digit = grade // 10
extra = ''
if ones_digit < 5:
    extra = '-'
elif ones_digit > 5:
    extra = '+'

if grade >= 90:
    print('A' + extra)
elif grade >= 80:
    print('B' + extra)
elif grade >= 70:
    print('C' + extra)
elif grade >= 60:
    print('D' + extra)
else:
    print('F')