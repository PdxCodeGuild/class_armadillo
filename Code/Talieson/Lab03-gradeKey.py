run = True

while run:
    run = False
    grade = input("Enter a number grade to converet it to a letter grade:")
    if not grade.isnumeric():
        print("That's not a number! Please enter a number.")
        run = True

    else:
        grade = int(grade)
        secondDigit = grade % 10
        leadingMark = ''
        if secondDigit >= 7 and grade > 59:
            leadingMark = '+'
        elif secondDigit <= 2 and grade > 59:
            leadingMark = '-'

        if grade >= 90:
            print('Good job! You got an A' + leadingMark + '!')
        elif 90 > grade >= 80:
            print('Good work. You got a B' + leadingMark + '.')
        elif 80 > grade >= 70:
            print('Hey, it gets the degree. You got a C' + leadingMark + '.')
        elif 70 > grade >= 60:
            print('Please review the lessons, you got a D' + leadingMark + '.')
        else:
            print('I\'ll see you in summerschool. You got an F.')
