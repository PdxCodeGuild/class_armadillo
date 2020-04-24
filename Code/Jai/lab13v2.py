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
    operated_num_list = operated_num.split() #in this variable the operated num is the number that the user chooses plus the operation that they'd like to perform. i split the input into a list so that they can work together. 
    # print(operated_num_list)
    
    operation = operated_num_list[0] #i pulled the operation from the Operated_num_list and put it in its own variable so that it can be read in an if statement on its own. 
    
    user_num = float(operated_num_list[1]) #pulled the number out of the operated num list and wrapped it in a float so that it can be readable in my if statement. 
    
#simple if statement to do the arithmatic and there we have it. a simple calculator..version 2. :)

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