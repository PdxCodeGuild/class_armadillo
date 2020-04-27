import time
from colorama import Fore

print('\nWelcome to CALCULATOR!')

time.sleep(1)

while True: # input validation for first number
    num = input('What is the first number? ') # will be the running number
    if num.isnumeric() == False: # checks if entered value is a number
        print(Fore.RED + '\nInvalid input!\n' + Fore.RESET) # if not a number prints invalid msg in red
    else: 
        num = float(num) # if value is a number, it gets converted to float here since isnumeric can check strings only
        break

signs = ['+', '-', '*', '/'] # list of valid operators for input validation

while True:
    operation_nextnum = input('What is the operation (+, -, * or /) and next number? (for example, \'+ 4\') ') # requires space
    operation_nextnum = operation_nextnum.split(' ') # splits the string into list on ' ' delimiter
    operation = operation_nextnum[0] # +, -, * or /
    if operation in signs and operation_nextnum[1].isnumeric() == True: #input validation for operation and next number
        nextnum = float(operation_nextnum[1]) # if operation and next num pass validation, converts next num to float
        if operation == '+':
            num += nextnum # running number
        elif operation == '-':
            num -= nextnum
        elif operation == '*':
            num *= nextnum
        elif operation == '/':
            num /= nextnum
    else:
        print(Fore.RED + '\nInvalid input!\n' + Fore.RESET)
    print(num) # running number prints after each operation
        
 


'''
Lab 13: Simple Calculator

Version 1
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, 
multiplication, and division. Ask the user for an operator and each operand. 
Don't forget that input returns a string, which you can convert to a float using float(user_input)
where user_input is the string you got from input. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!

Version 2  # 4/14 4.03.32
Allow the user to enter a running menu

> what is the starting number? 34
> enter operation: + 10
> 44
> enter operation: * 3
> 132

Version 3 (optional)
Allow the user to write an expression, alternating numbers and operators. Evaluate the expression left-to-right.

> what is the expression? 5 + 6 * 2
> 22

Version 4 (optional)
Allow the user to write an expression, alternating numbers and operators. Follow the proper order of operations, evaluating first exponentiation, then multiplication and division, then addition and subtraction.

> what is the expression? 5 + 6 * 2
> 17

Version 5 (optional)
Allow the user to write an expression including parantheses.

> what is the expression? 5*(6 + 2)
> 40
'''