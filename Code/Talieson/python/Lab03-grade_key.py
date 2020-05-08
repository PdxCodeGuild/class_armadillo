# This grade key takes a number grade and converts it to a letter grade.

# this main loop takes the input and validates the input is a number.
while True:
    grade = input("Enter a number grade to converet it to a letter grade:")
    if grade.isnumeric():
        break
    print("That's not a number! Please enter a number.")

# Here we convert the grade to an integer from a string of digits
grade = int(grade)
# Use modulus to identify the second digit for adding + or -
secondDigit = grade % 10
# sets an empty variable for leading mark to be filled in if needed.
leadingMark = ''

# check if that second digit justifies applying a + or -
if secondDigit >= 7 and grade > 59:
    leadingMark = '+'
elif secondDigit <= 2 and grade > 59:
    leadingMark = '-'

# Check the original input to identify what letter grade and return it.
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
