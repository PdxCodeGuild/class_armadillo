# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, 
# # multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a 
# string, which you can convert to a float using float(user_input) where user_input is the string you got from input. 
# Below is some sample input/output.

# > what is the operation you'd like to perform? +
# > what is the first number? 5
# > what is the second number? 12
# > 5 + 12 = 17
# > what is the operation you'd like to perform? done
# > goodbye!

#def cleaner():

# Initial variables & lists
which_operator = ""
num1 = ""
num2 = ""
list_mult = ["*", "multiply", "multiplication"]
list_div = ["/", "division", "divide"]
list_add = ["+", "add", "addition"]
list_sub = ["-", "subtract", "subtraction"]
kill_list = ["done", "end", "quit", "exit"]

operators = [list_mult, list_div, list_add, list_sub]

# def endgame():
#     print("Goodbye!")
#     quit()

print("Welcome to Lab 13. Let's do math. ")

# def get_inputs():
if not which_operator in operators:
    which_operator = input("What operation would you like to perform? ").lower().split()

num1 = float(input("What's the first number? "))
num2 = float(input("What is the second number? "))

# def do_math():
if which_operator in list_mult:
    total = num1 * num2
    print(f'{num1} * {num2} = {total}')
elif which_operator in list_div:
    total = num1 / num2
    print(f'{num1} / {num2} = {total}')
elif which_operator in list_add:
    total = num1 + num2
    print(f'{num1} + {num2} = {total}')
elif which_operator in list_sub:
    total = num1 - num2
    print(f'{num1} - {num2} = {total}')
elif which_operator in kill_list:
    endgame()



# while True:
#     get_inputs()
#     do_math()
