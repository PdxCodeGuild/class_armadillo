# Lab 13 Simple Calculator
# Troy Fitzgerald
# 

'''Version 2'''
'''Allow the user to have a running value, each command will 
perform an operation on that number.'''

# imports modules
import random
import math
# defines the function.
def calculator():
    # has the user enter their first number.
    number_1 = int(input('What is your starting number? '))
    # starts the while loop if the conditions below are true.
    while True:
        # has user enter what operation they want to do (+, -, *, \).
        operation = input('What math function would you like to perform? ')
        number_2 = int(input('What is your next number? '))
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
        