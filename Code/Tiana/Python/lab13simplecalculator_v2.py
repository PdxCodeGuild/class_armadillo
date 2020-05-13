#Lab 13: Simple Calculator Version 2

# Allow the user to have a running value, each command will perform an operation on that number.

# > what is the starting number? 34
# > enter operation: + 10
# > 44
# > enter operation: * 3
# > 132

running_value = float(input('Enter a number to start with: '))

while True:

    operator = input('What operation would you like to perform? ')
    if operator == 'none':
        print('Alright!')
        break
    
    num2 = float(input('Enter another number to use with operator: '))


    if operator == "+":
        value = running_value + num2
    elif operator == "-":
        value = running_value - num2
    elif operator == "*":
        value = running_value * num2
    elif operator == "/":
        value = running_value / num2

    running_value = value
    print(value)
    


