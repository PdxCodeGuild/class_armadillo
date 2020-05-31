
# lab 13

# https://stackoverflow.com/questions/48134055/python-function-returns-none-in-elif-or-else

# https://levelup.gitconnected.com/3-ways-to-write-a-calculator-in-python-61642f2e4a9a

#this lab allows user to perform calculation using add, subtract, multiply, or divide

performing = True

while performing:


    first = float(input("What is your first number? ")) #takes user first num in float
    second = float(input("What is your second number? "))  #takes user second num in float
    thing = input("What to do with these two numbers? 'add', 'subtract', 'multiply', 'divide'? ")  #takes user operations

    if thing.lower() == "add" or thing == "+":  #user can enter string or symbol
        answer = first + second 
        print(first, "+", second, "=", answer)  #sum inputs

    elif thing.lower() == "subtract" or thing == "-":
        answer = first - second
        print(first, "-", second, "=", answer)  #subtract inputs

    elif thing.lower() == "multiply" or thing == "*":
        answer = first * second    
        print(first, "*", second, "=", answer)  #multiply inputs

    elif thing.lower() == "divide" or thing == "/":
        answer = first / second
        print(first, "/", second, "=", answer)  #divide inputs 

    else:
        print("Invalid Entry")  #if user enters something that is not authorized    

    another_calc = input("Continue or type 'quit': ")  #allows user to start over
    if another_calc == "quit":
        print("Onwards and upwards!")
        break   
   
    



# op = input("What is the thing to perform? ('/', '*', '+', '-'): ")

# first = int(input("What is the first number? : "))
# second = int(input("What is the second number? : "))

# out = None

# if op == '/':
#     out = (first/second)

# elif op == '*':
#     out = first * second

# elif op == '-':
#     out = first - second

# elif op == '+':
#     out = first + second

# else:
#     print("not a valid operator")


# print(str(out))
