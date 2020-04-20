

#Ask the user for an operator.
choice = input("Enter choice (+, -, *, /): ")

print(choice)

#Input returns a string which you convert to float using 
# float (user_input).
num_0 = int(input("What is the first number? "))
print(num_0)

num_1 = int(input("What is the second number? "))
print(num_1)

if choice == "+":
    print(num_0, "+", num_1, "=", (num_0 + num_1))

elif choice == "-":
    print(num_0, "-", num_1, "=", (num_0 - num_1))

elif choice == "*":
    print(num_0, "*", num_1, "=", (num_0 * num_1)) # equivalent to num_0 + "*" + num_1 + "=" (num_0 * num_1))

elif choice =="/":
    print(num_0, "/", num_1, "=", (num_0 / num_1))
