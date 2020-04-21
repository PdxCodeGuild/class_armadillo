"""
Lab 13: Simple Calculator

Version 1
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, 
subtraction, multiplication, and division. Ask the user for an operator and each operand. 
Don't forget that input returns a string, which you can convert to a float using 
float(user_input) where user_input is the string you got from input. Below is some sample 
input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!

Version 2
Allow the user to have a running value, each command will perform an operation on that number.

> what is the starting number? 34
> enter operation: + 10
> 44
> enter operation: * 3
> 132

"""

while True:
    operator = input("What is the operation you'd like to perform? (+, - , *, /) ")

    first_num = float(input("What is the first number? "))

    second_num = float(input("What is the second number? "))

    if operator == "+":
        result = (f"{first_num} + {second_num} = {first_num+second_num}")

    elif operator == "-":
        result = (f"{first_num} - {second_num} = {first_num-second_num}")

    elif operator == "*":
        print(f"{first_num} * {second_num} = {first_num*second_num}")

    elif operator == "/":
        print(f"{first_num} / {second_num} = {first_num/second_num}")
    else:
        print("Something went wrong. Please, try again. ")


        

