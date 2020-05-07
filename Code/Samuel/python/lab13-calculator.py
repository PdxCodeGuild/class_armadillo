# PDX Code Guild Fullstack Course
# Lab 13 Calculator Version 1-2
# Samuel Purdy
# 4/14/2020

import string

user_input = None


# Returns a number based on the number given, and the expression given.
def do_math(number, expression):
    expression = expression.replace(" ", "")

    # Looks through the expression for a character, and based on that
    # character, it will do the operation.
    # since expression is a string, we want to read everything after the
    # operator, so we use expression[1:] to return the entire number
    # after the operator. We use this expression in order to return the
    # entire number instead of the first number after the operator.
    if expression.find("*") > -1:
        return float(number) * float(expression[1:])
    elif expression.find("/") > -1:
        return float(number) / float(expression[1:])
    elif expression.find("+") > -1:
        return float(number) + float(expression[1:])
    elif expression.find("-") > -1:
        return float(number) - float(expression[1:])
    elif expression.find("^") > -1:
        return float(number) ** float(expression[1:])


user_input = input("What is the number?  ")
user_expression = None

while True:
    # Checks to make sure the input is not blank, or it does not contain 
    # alphabetical characters.
    while user_expression == None or user_expression.isalpha():
        user_expression = input("What is the expression? (\"done\" if you want to exit.) ")
        # Exits the program if the input is done.
        if user_expression == "done":
            exit()

    # Each time the expression is calculated, it is saved to the old number in
    # order to do more expressions so long as the user inputs an expression.
    user_input = do_math(user_input, user_expression)
    user_expression = None

    print(user_input)
