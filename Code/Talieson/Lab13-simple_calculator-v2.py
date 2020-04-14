from calculator_math import *

# intro message.
print("#="*45)
print(''' Welcome to Calcutron - enter a an operator and a number seperated by a space to 
recieve an answer. Currently exceptable operators are +, -, *, and /. ''')
print("#="*45)

# start main run loop.
run = True
running_value = None

while run:
    if not running_value:
        # take the inital input that will become our running total.
        running_value = float(input("what is the starting value? "))
    
    # take the operator and the operating value
    operator, second_number = input("enter operation: ").split(" ")
    second_number = float(second_number)

    # check which operator is being used and use the applicable arrithmatic.
    if operator == "+":
        running_value = addition(running_value, second_number)
    elif operator == "-":
        running_value = subtraction(running_value, second_number)
    elif operator == "*":
        running_value = multiplication(running_value, second_number)
    elif operator == "/":
        running_value = division(running_value, second_number)

    # return the result.
    print(f"Your answer is {running_value}.")

    # end the run and check if there is more to do.
    run = False
    while not run:
        repeat = input("Would you like to perform another operation? (Y/N) ")
        if repeat == "Y":
            run = True
            break
        if repeat == "N":
            print("Thanks for coming by!")
            exit()
        else:
            print("please enter a valid response")