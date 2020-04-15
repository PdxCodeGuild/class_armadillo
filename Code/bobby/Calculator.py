import time


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
       print(num1,"+",num2,"=", (num1 + num2))

    elif choice == '-':
       print(num1,"-",num2,"=", (num1 - num2))

    elif choice == '*':
       print(num1,"*",num2,"=", (num1 * num2))

    elif choice == '/':
       print(num1,"/",num2,"=", (num1 / num2))
    else:
       print("\nInvalid input")# If user types in anything outside of the defined opoerations, they will get this message at the end.
    cont = input("\nWould You Like to Select a New Operation?y/n: ") #To restart or end program
else:
    print("\nGood Bye!") #If user ends the program they are given a Good Byw message