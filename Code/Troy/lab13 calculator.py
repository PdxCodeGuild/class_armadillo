'''Let's write a simple REPL (read evaluate print loop) calculator 
that can handle addition, subtraction, multiplication, and division. 
Ask the user for an operator and each operand. Don't forget that input 
returns a string, which you can convert to a float using float(user_input) 
where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17'''


import random
import math
import time

def calculator():

# starts the while loop if the conditions are True.
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
# starts the second while loop if the conditions are True.       
while True:
# has the user input if they wish to use the calculator.    
    user_answer = input('Do you wish to use the calculator? ')
# processes the user's answers to ensure they are valid responses.  If not, it ask the unser for a valid respons.   
    if user_answer in ['yes','y']:
        calculator()
    elif user_answer in ['no', 'n']:
        print('Goodbye!')
        break
    else:
        print('Please enter a valid response of yes, y, no, or n!')
        

'''Version 2'''
# has the user enter their starting number.
number_1 = int(input('What is your starting number? '))

# starts the while loop if the conditions are True.
while True:
# asks the user what math function they with to perform.
    operation = input('What math function would you like to perform? ')
# asks the user what number they wish to input.
    number_2 = int(input('What is your next number? '))
# processes the user's input and completes the math function while keeping the original number input.
    if operation == '+':
        number_1 += number_2
        print(number_1) 
    elif operation == '-':
        number_1 -= number_2
        print(number_1) 
    elif operation == '*':
        number_1 *= number_2
        print(number_1) 
    elif operation == '/':
        number_1 /= number_2
        print(number_1)  


