#lab13-calculator-v1 sample by the instructor: 

operator = input('what is the operator? ')
operand1 = float(input('what is the first operand? '))
operand2 = float(input('what is the second operand? '))
result = None
if operator == '+':
  result = operand1 + operand2
elif operator == '-':
  result = operand1 - operand2
elif operator == '*':
  result = operand1 * operand2
elif operator == '/':
  result = operand1 / operand2

print(f'{operand1}{operator}{operand2} = {result}')