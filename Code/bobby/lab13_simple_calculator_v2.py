# Lab 13 Version 2 Simple Calculator

import time

print("Welcome to My Calculator V.2 \n")
time.sleep(2)
print("Your List of Operators: \n + \n - \n * \n / \n")

# This is wher the user inputs their first digit into the calculator.
value = float(input("What is your first number? "))

# The beginning of the loop if user wants to continue adding to the calculation.
while True:
    # User enters the operator they wish to use, or types done if they are finished with their calculation. 
    # If the user whishes to add to the previous calculation all they have to do is enter the next operator the y whis to use.
    operation = input("What operation would like to perform? Or type 'done' to exit: ")
    # If user decides they do not want to continue this will break the loop and end the program.
    if operation == 'done':
        break
    # This is where the user would enter the next numerical digit into the calculation.
    value2 = float(input("What is your second value? "))
    # This section is the mathmatical portion that dictates how each operator will work based on user input.
    if operation.lower() == "add" or operation == "+":
        value += value2
    elif operation.lower() == "subtract" or operation == "-":
        value -= value2
    elif operation.lower() == "multiply" or operation == "*":
        value *= value2
    elif operation.lower() == "divide" or operation == "/":
        value /= value2
    print(value + value2)

    # I tried a few differnt ways to have the end result print out like it did in my previous 
    # version (56.0 + 44.0 = 100) but as of now have been unsuccessful.
