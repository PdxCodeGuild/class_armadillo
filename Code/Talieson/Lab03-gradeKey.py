run = True

while run:
    run = False
    numGrade = input("Enter the number grade to have it convereted to a letter grade:")
    if not numGrade.isnumeric():
        print("please enter a number")
        run = True

    else:
        numGrade = int(numGrade)
        secondDigit = numGrade % 10 
        leadingMark = ''
        if secondDigit >= 7 and numGrade > 59:
            leadingMark = '+'
        elif secondDigit <= 2 and numGrade > 59:
            leadingMark = '-'

        if numGrade >= 90:
            print('Good job! You got an A' + leadingMark + '!')
        elif 90 > numGrade >= 80:
            print('Good work. You got a B' + leadingMark + '.')
        elif 80 > numGrade >= 70:
            print('Hey, it gets the degree. You got a C' + leadingMark + '.')
        elif 70 > numGrade >= 60:
            print('You should review the matierial again, you got a D'  + leadingMark + '.')
        else:
            print('I\'ll see you in summerschool. You got an F.')
        

