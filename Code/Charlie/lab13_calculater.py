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

calc = input("Type calculation:\n")

print("Answer: " + str(calculate(calc)))
