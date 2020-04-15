#Lab 13: Simple Calculator


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


# Version 1

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
    


# Version 2

# Allow the user to have a running value, each command will perform an operation on that number.

# > what is the starting number? 34
# > enter operation: + 10
# > 44
# > enter operation: * 3
# > 132
# """
# #Version 2 

#def
# def cont_calculating(): 
    
#     cont = input('Would you like to continue using the calculator? Y/N: ')
#     if cont == 'n' or cont == 'N':
#         print('Thank you! see you soon Goodbye! ')
#         return False
#     return True

# running_value = float(input('What is the starting number? '))
# while True:
#     operation = input('Enter one of the following math operation symbols: ( +, -, *, or / ):  ')
#     if operation == "done":
#         break
#     operation = operation.split(' ') # this is to allow the user to enter math operator plus a number like + 10 with a space in between + and 10
#     math_operator  = operation[0] # the first item in the list    
#     operador = float(operation[1])
#     # mode = input('')
#     # num1 = float(input('Enter first number: '))
#     # num2 = float(input('Enter second number: '))

#     if math_operator == '+':
#         running_value += operador
#            # print(f'Answer is: {num1 + num2}')
#     elif math_operator == '-':
#         #print(f'Answer is: {num1 - num2}')
#         running_value -= operador
#     elif math_operator == '*':
#             #print(f'Answer is: {num1 * num2}')
#             running_value *= operador
#     elif math_operator == '/':
#         running_value /= operador
#             #print(f'Answer is: {num1 / num2}')
#     # else:
#     #     #print('Entered an invalid operation symbol! ( +, -, *, / ) :)')
#     # if not cont_calculating():
#     print(running_value)
    

