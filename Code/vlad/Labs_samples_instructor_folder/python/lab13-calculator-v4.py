

# 5 + 6 * 2
# 5 + 12
# 17

# 5 + 4 / 4 * 20 ** 2
# 5 + 4 / 4 * 400
# 5 + 1 * 400
# 5 + 400
# 405

operators = [
  ['**', '^'],
  ['*', '/'],
  ['+', '-']
]


expression = '5 + 4 / 4 * 20 ** 2' # input('what is the expression? ')
expression = expression.split(' ')
for i in range(0, len(expression), 2):
  expression[i] = float(expression[i])



def add(a, b):
  return a + b


# print(add(5, 2))
# print(add(5, 6))
# print(add(100, 1))


# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#   print(i, numbers)
#   if numbers[i] >= 2 and numbers[i] <= 3:
#     numbers.pop(i)
# print(numbers)



print(expression)
for operator_set in operators:
  i = 0
  while i < len(expression):
    if expression[i] in operator_set:
      operator = expression[i]
      operand1 = expression[i-1]
      operand2 = expression[i+1]
      result = None
      if operator == '+':
        result = operand1 + operand2
      elif operator == '-':
        result = operand1 - operand2
      elif operator == '*':
        result = operand1 * operand2
      elif operator == '/':
        result = operand1 / operand2
      elif operator == '**' or operator == '^':
        result = operand1 ** operand2
      
      expression.pop(i-1)
      expression.pop(i-1)
      expression.pop(i-1)
      expression.insert(i-1, result)
      i -= 2
      print(expression)
    i += 1



