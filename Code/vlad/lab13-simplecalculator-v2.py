#Lab 13: Simple Calculator Version 2



#Version 2

# make  first while loop a function and then after
# run that function return the answer that is given so it will look something like the example below:


def cont_calculating(): 
    
    cont = input('Would you like to continue using the calculator? Y/N: ')
    
    if cont == 'n' or cont == 'N':
        print('Thank you! see you soon Goodbye! ')
        return False
    
    return True
num1 = float(input('Enter first number: '))   
while True:
    print('Welcome to the world best carculator!: ')        
    mode = input('Enter one of the following math operation symbols: ( +, -, *, or / ): ')
    
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
        num1 += num2
    
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
        num1 -= num2
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
        num1 *= num2

    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
        num1 /= num2
    else:
        print('Entered an invalid operation symbol! ( +, -, *, / ) :)')
    if not cont_calculating():
        break
