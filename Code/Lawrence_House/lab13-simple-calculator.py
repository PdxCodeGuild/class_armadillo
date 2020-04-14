## Version 1

#Let's write a simple REPL (read evaluate print loop) calculator that can handle addition,
#  subtraction, multiplication, and division. Ask the user for an operator and each operand.
#  Don't forget that `input` returns a `string`, which you can convert to a float using
#  `float(user_input)` where `user_input` is the string you got from `input`.
#  Below is some sample input/output.


'''
> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
'''
#while True:
#    operator = input('What is the operation you\'d like to perform? ')
#    
#    if operator == 'done':
#        print('Goodbye!')
#        break
#
#    num1 = float(input('What is the first number? '))
#    
#    num2 = float(input('What is the second number? '))
#    
#    if operator == '+':
#        print(num1 + num2)
#    if operator == '-':
#        print(num1 - num2)
#    if operator == '*':
#        print(num1 * num2)
#    if operator == '/':
#        print(num1 / num2)


#   Version 2  Allow the user to enter a running menu

'''
> what is the starting number? 34
> enter operation: + 10
> 44
> enter operation: * 3
> 132
'''

while True:
     = input('What is the operation you\'d like to perform? ')
    
    if operator == 'done':
        print('Goodbye!')
        break

    num1 = float(input('What is the first number? '))
    
    num2 = float(input('What is the second number? '))
    
    if operator == '+':
        print(num1 + num2)
    if operator == '-':
        print(num1 - num2)
    if operator == '*':
        print(num1 * num2)
    if operator == '/':
        print(num1 / num2)