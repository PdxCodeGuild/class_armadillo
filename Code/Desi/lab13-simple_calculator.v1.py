

#Ask the user for an operator.
# choice = input("Enter choice (+, -, *, /): ")

# print(choice)

# #Input returns a string which you convert to int using 

# num_0 = int(input("What is the first number? "))
# print(num_0)

# num_1 = int(input("What is the second number? "))
# print(num_1)

# # simple REPL (read evaluate print loop) calculator that can
# #   handle addition, subtraction, multiplication, and division.

# if choice == "+":
#     print(num_0, "+", num_1, "=", (num_0 + num_1))

# elif choice == "-":
#     print(num_0, "-", num_1, "=", (num_0 - num_1))

# elif choice == "*":
#     print(num_0, "*", num_1, "=", (num_0 * num_1)) # equivalent to num_0 + "*" + num_1 + "=" (num_0 * num_1))

# elif choice =="/":
#     print(num_0, "/", num_1, "=", (num_0 / num_1))



# version 2


def calculator():
  

    num_0 = int(input("What is the first number? "))
    choice = input("Enter an operation you'd like to use for processing math.  ")
    num_1 = int(input("What is the second number? "))
    

    if choice == "-":
        answer = num_0 - num_1
        print(f"{num_0} {choice} {num_1} = {answer}")

    elif choice == "+":
        answer = num_0 + num_1
        print(f"{num_0} {choice} {num_1} = {answer}")    

    elif choice == "/":
        answer = num_0 / num_1
        print(f"{num_0} {choice} {num_1} = {answer}")
         

    elif choice == "*":
        answer = num_0 * num_1
        print(f"{num_0} {choice} {num_1} = {answer}")
           

    else: 
            print("\nI don't understand that, try again... ")

        
calculator()

 
   

    # if choice == "+":
    #     print(num_0, "+", num_1, "=", (num_0 + num_1))

    # elif choice == "-":
    #     print(num_0, "-", num_1, "=", (num_0 - num_1))

    # elif choice == "*":
    #     print(num_0, "*", num_1, "=", (num_0 * num_1)) # equivalent to num_0 + "*" + num_1 + "=" (num_0 * num_1))

    # elif choice =="/":
    #     print(num_0, "/", num_1, "=", (num_0 / num_1))