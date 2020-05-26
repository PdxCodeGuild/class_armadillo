
# lab 13

# https://stackoverflow.com/questions/48134055/python-function-returns-none-in-elif-or-else

# https://levelup.gitconnected.com/3-ways-to-write-a-calculator-in-python-61642f2e4a9a

op = input("What is the operation to perform? ('/', '*', '+', '-'): ")

first = int(input("What is the first number? : "))
second = int(input("What is the second number? : "))

out = None

if op == '/':
    out = (first/second)

elif op == '*':
    out = first * second

elif op == '-':
    out = first - second

elif op == '+':
    out = first + second

else:
    print("not a valid operator")


print(str(out))
