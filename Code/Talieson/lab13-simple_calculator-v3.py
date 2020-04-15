from calculator_math import *

# values = []
# operators = []

# user_input = input("enter your expression: ").split(" ")

# for i in user_input:
#     if i == "+" or i == "-" or i == "*" or i == "/":
#         user_input.remove(i)
#         operators.append(i)
#     if i.isnumeric():
#         i = int(i)
#         values.append(i)

# print(values)
# print(type(values[0]))
# print(operators)


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
