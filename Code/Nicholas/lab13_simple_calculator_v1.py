#this lab allows user to perform calculation using add, subtract, multiply, or divide

more_calc = True  #while loops allows for another calculation after initial one
while more_calc:


    user_num1 = float(input("What is your first number? ")) #takes user first num in float
    user_num2 = float(input("What is your second number? "))  #takes user second num in float
    operation = input("What operation would you like to execute? Select Add, Subtract, Multiply, or Divide: ")  #takes user operations

    if operation.lower() == "add" or operation == "+":  #user can enter string or symbol
        answer = user_num1 + user_num2 
        print(user_num1, "+", user_num2, "=", answer)  #sum inputs

    elif operation.lower() == "subtract" or operation == "-":
        answer = user_num1 - user_num2
        print(user_num1, "-", user_num2, "=", answer)  #subtract inputs

    elif operation.lower() == "multiply" or operation == "*":
        answer = user_num1 * user_num2    
        print(user_num1, "*", user_num2, "=", answer)  #multiply inputs

    elif operation.lower() == "divide" or operation == "/":
        answer = user_num1 / user_num2
        print(user_num1, "/", user_num2, "=", answer)  #divide inputs 

    else:
        print("Invalid Entry")  #if user enters something that is not authorized    

    another_calc = input("Make another calculation or type 'done' to exit: ")  #allows user to start over
    if another_calc == "done":
        print("Good bye!")
        break   
   
    
