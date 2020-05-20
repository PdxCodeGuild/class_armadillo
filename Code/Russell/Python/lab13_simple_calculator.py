# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, 
# subtraction, multiplication, and division.
#  Ask the user for an operator and each operand. 
#  Don't forget that input returns a string, 
#  which you can convert to a float using float(user_input) where user_input is the string you got from input. 
#  Below is some sample input/output.

# > what is the operation you'd like to perform? +
# > what is the first number? 5
# > what is the second number? 12
# > 5 + 12 = 17
# > what is the operation you'd like to perform? done
# > goodbye!

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def subtract(a, b):
#     return a - b

# def add(a, b):
#     return a + b

def calculate():
    while True:
        operation =  input('What is the operation you would like to perform? Add, Subtract, Divide, Multiply or type Done').lower()
        if operation == 'done':
            break
        first_number = float(input('What is the first number?'))
        second_number = float(input('What is the second number?'))

        if operation == 'add':
            print(f'{first_number} + {second_number} is {first_number + second_number}')
            

        elif operation == 'subtract':
            print(f'{first_number} - {second_number} is {first_number - second_number}')


        elif operation == 'divide':
            print(f'{first_number} / {second_number} is {first_number / second_number}')


        elif operation == 'multiply':
            print(f'{first_number} * {second_number} is {first_number * second_number}')
   
   
calculate()   







