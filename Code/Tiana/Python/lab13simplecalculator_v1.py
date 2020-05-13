#Lab 13: Simple Calculator Version 1

#Let's write a simple REPL (read evaluate print loop) calculator that can handle 
#addition, subtraction, multiplication, and division.

while True:
    #Ask the user for two numbers to operate on
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    #Ask the user for the operation to use
    operator = input('Enter a operation from +, -, /, *  ')
    #Calculate numbers with operator based off of input
    if operator == "+":
        total = (num1 + num2)
        print(total)
    elif operator == "-":
        total = (num1 - num2)
        print(total)  
    elif operator == "*":
        total = (num1 * num2)
        print(total)
    elif operator == "/":
        total = (num1 / num2)
        print(total)
    #Give the user a option to play again
    repeat = input('Would you like to play again? ')
    if repeat == 'no':
        print('Alright!')
        break





