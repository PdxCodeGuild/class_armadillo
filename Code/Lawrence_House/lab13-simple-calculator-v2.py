#   Version 2  Allow the user to enter a running menu

running_number = int(input('What is the running number? '))     # Running Value

while True:
    
    operator = input('What is the operator? ')   # Operator for the equation. (e.g +, -, *, /)

    if operator == ('done'):    # exit statement
        print('Goodbye!')
        break    

    num2 = float(input('What is the second number? '))

    #  Completes operation and prints result

    if operator == '+':
        answer = running_number + num2
    if operator == '-':
        answer = running_number - num2
    if operator == '*':
        answer = running_number * num2
    if operator == '/':
        answer = running_number / num2
    print(answer)
    running_number = answer # Next operation will run based on this number