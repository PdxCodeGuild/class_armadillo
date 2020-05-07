from operator import pow, truediv, mul, add, sub 

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

def calculate(user_input):
   if user_input.isdigit():
      return float(user_input)

   for i in operators.keys():
      input1, operator, input2 = user_input.partition(i)
      if operator in operators:
         return operators[operator](calculate(input1), calculate(input2))
   

# def again():
#    calc_again = input("Do you want to enter another calculation?\nPlease type y for YES or n for NO: ")
#    if calc_again == 'y':
#       calculate(calc)
#    else:
#       print('See you later.')


def main():
   while True:
      calc = input("Type calculation you want sloved then press enter:\n")
      print(f'{calc} = {str(calculate(calc))}')

      calc_again = input("Do you want to enter another calculation?\nPlease type y for YES or n for NO: ")
      if calc_again == 'y':
         continue
      else:
         print('See you later.')
         break
main()
   