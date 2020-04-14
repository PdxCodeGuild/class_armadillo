op = input("What is the operation to perform? : ")
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

def operand(i):
    switcher = {
        1: 'add',
        2: 'subtract',
        3: 'multiply',
        4: 'divide',
    }
    return switcher.get(i, "invalid entry")

first = int(input("What is the first number? : "))
second = int(input("What is the second number? : "))

print(operand(0))

def add(first, second):
    return first + second
print(add(first,second) + 'is the sum')

# sum = (first + second)
# print(f'{sum} is the result')

# above only adds

def subtract(first, second):
    return first - second
print(subtract(first,second) + 'is the difference')

def multiply(first, second):
    return first * second
print(multiply(first,second) + 'is the product')

def divide(first, second):
    return first / second
print(divide(first,second) + 'is the quotient')