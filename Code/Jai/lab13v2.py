#created functions for the operations 
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b



starting_number = float(input("what is your starting number?: "))

while True: 
    operated_num = input('enter an operation; ')
    print(operated_num)
    operated_num_list = operated_num.split()
    print(operated_num_list)
    operation = operated_num_list[0]
    user_num = float(operated_num_list[1])
    if operation == '+':
        starting_number = add(user_num, starting_number)
        print(starting_number)
    elif operation == '-':
        starting_number = subtract(user_num, starting_number)
        print(starting_number)
    elif operation == '*':
        starting_number = multiply(user_num, starting_number)
        print(starting_number)
    elif operation == '/':
        starting_number = divide(user_num, starting_number)
        print(starting_number)
    else:
        break