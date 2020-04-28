#Lab 13 Simple Calculator Version 1
#4/14/2020

#Ask the user for an operator and each operand
while True:
    numb1 = float(input('Give a number: '))
    numb2 = float(input('Give another number: '))
    user_operand = input('Do you want to add, subtract, multiply, or divide? ')

#Calculations of the operands
    if user_operand == 'add':
        print(numb1 + numb2)
    elif user_operand == 'subtract':
        print(numb1 - numb2)
    elif user_operand == 'multiply':
        print(numb1 * numb2)
    elif user_operand == 'divide':
        print(numb1 / numb2)

#Allow the user to play again or be done
    question = input('Do you want to play again? If not say done ')
    if question == 'done':
        print('So Long!!')
        break
    else:
        continue