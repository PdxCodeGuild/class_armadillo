# what is the operation you'd like to perform? 
# what is the first number? 5
# what is the second number? 12    5 + 12 = 17
# what is the operation you'd like to perform? 


# Version 1
# what is the operation you'd like to perform?
user = input("Pick a random number and then put it into an operation such as +, -, *, or /: ")

def calc_nums():
    numbers = []


# what is the first number?
# This function adds two numbers 
def add(2, 7):
   return 2 + 7
print(add)

# This function subtracts two numbers 
def subtract(x, y):
   return x - y
print(subract)

# This function multiplies two numbers
def multiply(x, y):
   return x * y
print(multiply)

# This function divides two numbers
def divide(x, y):
   return x / y
print(divide)




num = input("Enter a number or 'done' ")
while myinput != "done":
    numbers.append(int(myinput))
    num = input("Enter a number or 'done' ")


return numbers
print(calc_nums())



# what is the second number?
def calc_nums():
    numbers = []
    numbers.append(input("Enter a number or 'done'")
print(calc_nums())


# what is the operation you'd like to perform? 





# Version 2
#what is the starting number? 34
user = input("I have a number for you and want you to go off 
that number. Enjoy!")
#enter operation: + 10      
#enter operation: * 3




# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")










Lab 13: Simple Calculator


Version 1
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!


Version 2
Allow the user to have a running value, each command will perform 
an operation on that number.

> what is the starting number? 34
> enter operation: + 10
> 44
> enter operation: * 3
> 132


Version 3 (optional)
Allow the user to write an expression, alternating numbers and operators. Evaluate the expression left-to-right.

> what is the expression? 5 + 6 * 2
> 22