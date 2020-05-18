
# user inputs their initial number which is altered in the while loop  
total = float(input('What is your starting number?'))

while True:
    operation = input('What operation would you like to perform? or type \'done\'')
    if operation == 'done':
        break
    
    operation = operation.split() #splits the operation sign and oporand to be assigned to two variables
    operation_sign = operation[0] 
    second_number = float(operation[1])
   
    # the total will + - * / by the second number until the user enters done 
    if operation_sign == '+':
        total += second_number
    
    elif operation_sign == '-':
        total -= second_number

    elif operation_sign == '*':
        total *= second_number
     
    elif operation_sign == '/':
        total /= second_number      

    print(total)
     
    




