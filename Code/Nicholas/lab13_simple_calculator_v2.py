
#this lab allows user to conduct simple calculation using add, subtract, multiply, and divide and then lets them perform more operations with a running total

value_running = float(input("What is your first number? "))  #takes first input
while True:  #loops back to here for more input to create running calculation
    operation_running = input("What operation would like to perform? Or type 'done' to exit: ") #takes second input
    if operation_running == 'done':  #option to leave program
        break 
    second_value = float(input("What is your second value? "))  #takes second input
    if operation_running.lower() == "add" or operation_running == "+":
        value_running += second_value  #adds to existing value
    elif operation_running.lower() == "subtract" or operation_running == "-":
        value_running -= second_value  #subs from existing value
    elif operation_running.lower() == "multiply" or operation_running == "*":
        value_running *= second_value  #mult from existing value  
    elif operation_running.lower() == "divide" or operation_running == "/":
        value_running /= second_value  #div from existing value 
    print(value_running)    
       
  
      
   
   
        

    




                      

            
   
