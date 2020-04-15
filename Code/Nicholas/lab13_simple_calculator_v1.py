more_calc = True
while more_calc:


    user_num1 = float(input("What is your first number? "))
    user_num2 = float(input("What is your second number? "))
    operation = input("What operation would you like to execute? Select Add, Subtract, Multiply, or Divide: ")

    if operation.lower() == "add" or operation == "+":
        answer = user_num1 + user_num2 
        print(user_num1, "+", user_num2, "=", answer)

    elif operation.lower() == "subtract" or operation == "-":
        answer = user_num1 - user_num2
        print(user_num1, "-", user_num2, "=", answer)

    elif operation.lower() == "multiply" or operation == "*":
        answer = user_num1 * user_num2    
        print(user_num1, "*", user_num2, "=", answer)

    elif operation.lower() == "divide" or operation == "/":
        answer = user_num1 / user_num2
        print(user_num1, "/", user_num2, "=", answer)   

    else:
        print("Invalid Entry")    

    another_calc = input("Make another calculation or type 'done' to exit: ")
    if another_calc == "done":
        print("Good bye!")
        break   
   
    
