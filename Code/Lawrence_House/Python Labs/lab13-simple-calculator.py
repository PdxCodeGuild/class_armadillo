## Version 1

#  Let's write a simple REPL (read evaluate print loop) calculator that can handle addition,
#  subtraction, multiplication, and division. Ask the user for an operator and each operand.

while True:
    operator = input('What is the operation you\'d like to perform? ')    # Operator for the equation. (e.g +, -, *, /)
    
    if operator == 'done':    # exit statement
        print('Goodbye!')
        break

    num1 = float(input('What is the first number? '))
    
    num2 = float(input('What is the second number? '))

    #  Completes operation and prints result
    
    if operator == '+':     
        print(num1 + num2)
    if operator == '-':
        print(num1 - num2)
    if operator == '*':
        print(num1 * num2)
    if operator == '/':
        print(num1 / num2)