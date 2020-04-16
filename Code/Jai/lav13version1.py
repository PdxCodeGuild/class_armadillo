

#created functions for the operations 
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b



#while true allows my calculator to loop forever
while True:
    operation = input("choose an operation (+, -, *, /), if not enter 'done': ") #the operation variable is going to equal whatever the user chooses for the operation. 
    if operation == 'done': #i put this in the while true statement so that if the user decided not to play and chose "done" it would end the game. 
    
        break
    
    num1 = float(input("what is your number? ")) #this is the first number that the user will work with

    num2= float(input("what is your second number? ")) #the second number in the eqution
    
    #used a simple if statement to determine the operation and what it does in the equation. 
    if operation == '+':
         print(add(num1,num2))

    elif operation == '-':
         print(subtract(num1,num2))

    elif operation == '*':
        print(multiply(num1, num2))
    
    elif operation == '/':
        print(divide(num1, num2))
    
    else:
        print("try using the operations provided! ") #just in case. 
        
        break


        