# Lab 13 Simple Calculator

# Import time modual, used to give user time 
# to read messages before running the next step of the program.
import time

# Welcome message.
print("Welcome to My Calculator.\n")
time.sleep(1)

#let the user know which operations are valid choices, and starting the while loop.
cont = "y"
while cont == "y" or cont == "Y":
    print("\nPlease Select Your Operation:")
    print("+")
    print("-")
    print("*")
    print("/")

    # Take input from the user 
    choice = input("\nEnter choice(+, -, *, /): ")

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("\nEnter second number: "))

    # The diffrent strings of input that produces the output
    if choice == '+':
       print(num1, "+" , num2, "=", (num1 + num2))

    elif choice == '-':
       print(num1,"-",num2,"=", (num1 - num2))

    elif choice == '*':
       print(num1,"*",num2,"=", (num1 * num2))

    elif choice == '/':
       print(num1,"/",num2,"=", (num1 / num2))
    else:      
       #if uder uses anything that is now an operator this message will show at end of opperation.
       print("\nInvalid input")
       
    cont = input("\nWould You Like to Select a New Operation?y/n: ")
else: 
   #If user ends the program they are given a Good Byw message
    print("\nGood Bye!") 