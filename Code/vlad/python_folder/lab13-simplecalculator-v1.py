#Lab 13: Simple Calculator Version 1


"""
Version 1
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, 
multiplication, and division. Ask the user for an operator and each operand. Don't forget 
that input returns a string, which you can convert to a float using float(user_input) where user_input 
is the string you got from input. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
"""


# # Version 1

def cont_calculating(): 
    
    cont = input('Would you like to continue using the calculator? Y/N: ')
    if cont == 'n' or cont == 'N':
        print('Thank you! see you soon Goodbye! ')
        return False
    return True
while True:
    print('Welcome to the world best carculator!: ')        
    mode = input('Enter one of the following math operation symbols: ( +, -, *, or / ): ')
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if mode == '+':
            print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
            print(f'Answer is: {num1 * num2}')
    elif mode == '/':
            print(f'Answer is: {num1 / num2}')
    else:
        print('Entered an invalid operation symbol! ( +, -, *, / ) :)')
    if not cont_calculating():
        break
    

