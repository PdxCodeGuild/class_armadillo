#lab13-calculator-v3 sample by the instructor: 

expression = '5 + 4 / 3 * 100' # input('what is the expression? ')
# print(eval(expression))
expression = expression.split(' ')
print(expression)
for i in range(0, len(expression), 2):
  expression[i] = float(expression[i])
print(expression)
running_number = expression[0] # take the first number as our starting number
print(running_number)
for i in range(1, len(expression), 2):
  operator = expression[i]
  operand = expression[i+1]
  print(operator, operand)
  
  if operator == '+':
    running_number += operand
  elif operator == '-':
    running_number -= operand
  elif operator == '*':
    running_number *= operand
  elif operator == '/':
    running_number /= operand
  print(running_number)
  print()