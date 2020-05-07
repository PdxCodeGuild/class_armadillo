

# Lab 2: Mad Libs


print("Welcome to Madlib")
# a-d will store whatever the input is 
a = input("Enter your name: ")
b = input("Enter favorite sport: ")
c = input("Favorite team name: ")
d = input("Enter city your team is from: ")
e = input("Enter name of favorite player: ")
d = input("Would you like to hear the story?: ")
# this f string puts all the input from the user into a string
madlib = f"My name is {a} and I am a {b} fan. {c} is the best and {d} is where the team is from {e} is the bestest ever!! "





# if user replys to d as yes yea sure it will print madlib else it will exit
if d in ["yes", "yeah", "sure"]:
    print(madlib)
else:
    print("goodbye")





