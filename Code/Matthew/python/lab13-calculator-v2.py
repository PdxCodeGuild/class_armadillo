

running_number = float(input('what is the starting number? '))
while True:
  operation = input('what is the operation? ') # + 32
  if operation == 'done':
    break
  operation = operation.split(' ')
  operator = operation[0]
  operand = float(operation[1])
  if operator == '+':
    running_number += operand
  elif operator == '-':
    running_number -= operand
  elif operator == '*':
    running_number *= operand
  elif operator == '/':
    running_number /= operand
  print(running_number)


