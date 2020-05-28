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
total = ""
list_mult = ["*", "multiply", "multiplication"]
list_div = ["/", "division", "divide"]
list_add = ["+", "add", "addition"]
list_sub = ["-", "subtract", "subtraction"]
list_all = ["*", "multiply", "multiplication", "/", "division", "divide", "+", "add", "addition", "-", "subtract", "subtraction"]
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape", "done"]
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way', "nah"]

# accessing elements from a list of lists not working...
operators = [list_mult, list_div, list_add, list_sub]

def endgame():
    print("Goodbye!")
    quit()


def get_inputs():
    which_operator = input("What operation would you like to perform? ").lower()
    while not which_operator in list_all:
        which_operator = input("What operation would you like to perform? ").lower()
    num1 = input("What's the first number? ")
    while not num1.isnumeric():
        print("That's not a valid answer. Choose a non-negative integer. I can't work with negatives or imaginary numbers at this time")
        num1 = input("What's the first number? ")
    num2 = input("What is the second number? ")
    while not num2.isnumeric():
        print("That's not a valid answer. Choose a non-negative integer. I can't work with negatives or imaginary numbers at this time")
        num1 = input("What's the second number? ")

    return which_operator
    return num1
    return num2


def do_math():
    print("made it step 2")
    print(f"Operand is '{which_operator}' .")
    print(f"First Number is {num1}. ")
    print(f"Second Number is {num2}. ")
    num1 = float(num1)
    num2 = float(num2)
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
    elif which_operator in kill_commands:
        endgame()

def calculator():
    while True:
        which_operator = input("What operation would you like to perform? ").lower()
        while not which_operator in list_all:
            which_operator = input("What operation would you like to perform? ").lower()
        num1 = input("What's the first number? ")
        while not num1.isnumeric():
            print("That's not a valid answer. Choose a non-negative integer. I can't work with negatives or imaginary numbers at this time")
            num1 = input("What's the first number? ")
        num2 = input("What is the second number? ")
        while not num2.isnumeric():
            print("That's not a valid answer. Choose a non-negative integer. I can't work with negatives or imaginary numbers at this time")
            num1 = input("What's the second number? ")
        break

    while True:
        # print(f"Operand is '{which_operator}' .")
        # print(f"First Number is {num1}. ")
        # print(f"Second Number is {num2}. ")
        num1 = float(num1)
        num2 = float(num2)
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
        elif which_operator in kill_commands:
            endgame()
        break
        

# asks the user if they want to play again.
def play_again():
    while True:
        ask_again = input("Would you like to play again? ")
        if ask_again.lower() in affirmatives:
            calculator()
        elif ask_again.lower() in negatives:
            print("Goodbye! ")
            break
        elif ask_again.lower() in kill_commands:
            endgame()
        else:
            print("I'm sorry, I don't understand that response. Please try again. ")

print("Welcome to Lab 13. Let's do math. ")

calculator()
play_again()

'''
while True:
    while True:
        which_operator = input("What operation would you like to perform? ").lower()
        while not which_operator in list_all:
            which_operator = input("What operation would you like to perform? ").lower()
        num1 = float(input("What's the first number? "))
        while not num1.isnumeric():
            print("That's not a valid answer. Choose a non-negative integer. I can't work with negatives or imaginary numbers at this time")
            num1 = float(input("What's the first number? "))
    #     return num1
        num2 = float(input("What is the second number? "))
        while not num2.isnumeric():
            print("That's not a valid answer. Choose a non-negative integer. I can't work with negatives or imaginary numbers at this time")
            num1 = float(input("What's the second number? "))
    #     return num2
    while True:
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
        elif which_operator in kill_commands:
            endgame()
        break
'''