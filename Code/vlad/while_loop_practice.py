#Practice while loop:

num = 76 # this can be any number
guess = 0
guess_limit= 5
guess_number = 0
guess = int(input(f'Guess a number 1-100:')) # guess = int(input(f'Guess a number 1-20 -1:')) by putting here -1 we counting only to 4
guess_number +=1
while guess_number < guess_limit: # while guess_number < guess_limit-1: by putting here -1 we counting only to 4
    if guess == num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} Too low - Guess again 1-100: '))
        print(f'You Win! You Guessed it {guess}')
    break # we break here if the user get it right and guess it if not then else

if guess != num:
    print(f'Sorry you lose! It was {num}')


    ################################################################################################


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


# Version 1 and Version 2

# def cont_calculating(): 
    
#     cont = input('Would you like to continue using the calculator? Y/N: ')
#     if cont == 'n' or cont == 'N':
#         print('Thank you! see you soon Goodbye! ')
#         return False
#     return True
# while True:
#     print('Welcome to the world best carculator!: ')        
#     mode = input('Enter one of the following math operation symbols: ( +, -, *, or / ): ')
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))

#     if mode == '+':
            
#         answer = print(f'Answer is: {num1 + num2}')
#         # return answer
#     elif mode == '-':
#         print(f'Answer is: {num1 - num2}')
#     elif mode == '*':
#             print(f'Answer is: {num1 * num2}')
#     elif mode == '/':
#             print(f'Answer is: {num1 / num2}')
#     else:
#         print('Entered an invalid operation symbol! ( +, -, *, / ) :)')
#     if not cont_calculating():
#         break
#     while True:
#         print('Welcome to the world best carculator!: ')        
#         mode = input('Enter one of the following math operation symbols: ( +, -, *, or / ): ')
#         num1 = float(answer)
#         num2 = float(input('Enter second number: '))

#         if mode == '+':
                
#             answer = print(f'Answer is: {num1 + num2}')
#         elif mode == '-':
#             print(f'Answer is: {num1 - num2}')
#         elif mode == '*':
#                 print(f'Answer is: {num1 * num2}')
#         elif mode == '/':
#                 print(f'Answer is: {num1 / num2}')
#         else:
#             print('Entered an invalid operation symbol! ( +, -, *, / ) :)')
#         if not cont_calculating():
#             break


"""
make  first while loop a function and then after
run that function return the answer that is given so it will look something like the example below:

def calc():
    while True:
        oper = input("")
        ans1 = input("")
        ans2 = input("")
        
        then have all your if statements 
        
        
    return the answer from the if statements
    
then write a new while loop below outside your fuction 
def running(answer):
    answer = float(answer)
    while true:
        and all the same stuff as before but for input 1 put it equal to answer
        ans = answer
"""

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
    

