"""
Lab 11: a simple REPL calculator
"""

while False:
    op = input('enter the operator (or \'done\') if done: ')
    if op == 'done':
        break
    else:
        num1 = float(input('what is the first number? '))
        num2 = float(input('what is the second number? '))
        if op == '+':
            print(num1+num2)
        elif op == '-':
            print(num1-num2)
        elif op == '*':
            print(num1*num2)
        elif op == '/':
            print(num1/num2)



# operations = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
#     '/': lambda a, b: a / b,
#     '**': lambda a, b: a ** b
# }
#
# operator = input('operator: ')
# operand1 = float(input('operand 1: '))
# operand2 = float(input('operand 2: '))
# # operator = operations[operator]
# # print(operator(operand1, operand2))
# print(operations[operator](operand1, operand2))







