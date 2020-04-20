#lab13-calculator-v1b sample by instructor:
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operators = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

operator = input('what is the operator? ')
operand1 = float(input('what is the first operand? '))
operand2 = float(input('what is the second operand? '))
result = operators[operator](operand1, operand2)

print(f'{operand1}{operator}{operand2} = {result}')