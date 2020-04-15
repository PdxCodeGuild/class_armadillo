from calculator_math import addition, subtraction, division, multiplication

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
