

while True:
    grade = input("Enter a number grade to converet it to a letter grade:")
    if grade.isnumeric():
        break
    print("That's not a number! Please enter a number.")

grade = int(grade)
secondDigit = grade % 10
leadingMark = ''

if secondDigit >= 7 and grade > 59:
    leadingMark = '+'
elif secondDigit <= 2 and grade > 59:
    leadingMark = '-'

if grade >= 90:
    print('Good job! You got an A' + leadingMark + '!')
elif grade >= 80:
    print('Good work. You got a B' + leadingMark + '.')
elif grade >= 70:
    print('Hey, it gets the degree. You got a C' + leadingMark + '.')
elif grade >= 60:
    print('Please review the lessons, you got a D' + leadingMark + '.')
else:
    print('I\'ll see you in summerschool. You got an F.')
