from calculator_math import addition, subtraction, division, multiplication

# simple calculator allows you to do very basic mathmatics.
# Version 2 changes the input to a single line.
# Version 3 allows the user to input multiple operators in a line.

expression = input("enter your expression: ").split(" ")
for i in range(0, len(expression), 2):
    expression[i] = float(expression[i])

running_value = expression[0]
for i in range(1, len(expression), 2):
    operator = expression[i]
    operand = expression[i+1]

    if operator == "+":
        running_value = addition(running_value, operand)
    elif operator == "-":
        running_value = subtraction(running_value, operand)
    elif operator == "*":
        running_value = multiplication(running_value, operand)
    elif operator == "/":
        running_value = division(running_value, operand)

print(running_value)
