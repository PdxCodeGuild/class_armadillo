# Lab 13 Simple Calculator
# Troy Fitzgerald
#

'''Let's write a simple REPL (read evaluate print loop) calculator 
that can handle addition, subtraction, multiplication, and division. 
Ask the user for an operator and each operand. Don't forget that input 
returns a string, which you can convert to a float using float(user_input) 
where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17'''

# imports modules.
import random
import math
# defines the function.
def calculator():
    # starts the while loop if the conditions below are true.
    while True:
        # has user enter what operation they want to do (+, -, *, \).
        user_question = input('What math function would you like to perform? ')
        
        # has the user enter their first number.
        user_input = int(input('What is your first number? '))

        # has the user enter their second number.
        user_next_input = int(input("What is your second number? "))

        # processes the math function and performs that function for user_input and user_next-input.
        if user_question == '+':
            total = user_input + user_next_input
            print(total)
        elif user_question == '-':
            total = user_input - user_next_input
            print(total)
        elif user_question == '*':
            total = user_input * user_next_input
            print(total)
        elif user_question == '/':
            total = user_input / user_next_input
            print(total)
# starts the second while loop to begin the process if the conditions are True.       
while True:
    # has the user input if they wish to use the calculator.    
    user_answer = input('Do you wish to use the calculator? ')
    # processes the user's answers to ensure they are valid responses.  If not, it ask the unser for a valid response.   
    if user_answer in ['yes','y']:
        calculator()
    elif user_answer in ['no', 'n']:
        print('Goodbye!')
        break
    else:
        print('Please enter a valid response of yes, y, no, or n!')
    
        
