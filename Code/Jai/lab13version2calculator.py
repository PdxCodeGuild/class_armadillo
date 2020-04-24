

#created functions for the operations 
def add(user_num, b):
    user_num += b 
    return user_num

def subtract(total, b):
    return user_num
def multiply(total, b):
    return user_num
def divide(user_num, b):
    return user_num


total = float(input("what is your starting number: "))
#while true allows my calculator to loop forever
while True:
    operation = input("choose an operation (+, -, *, /): ")
    user_num = float(input("what is your second number?: "))
    if operation == '+':
         total = add(user_num, total)
         print(total)

    elif operation == '-':
        subtract(user_num, num)
        print(user_num)
    elif operation == '*':
        multiply(user_num, num)
        print(user_num)
    elif operation == '/':
        divide(user_num, num)
        print(user_num)
    else:
        print("try using the operations provided! ") #just in case. 
        
        break









