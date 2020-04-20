import random

#the computer will generate a random int between
# 1 and 10. 
pc_guess = random.randint(1, 11)
#user will guess number between 1 and 10.

user_guess = int(input("Choose a random number betwee 1 and 10: "))

#using a while loop, allow user to guess 10 times.
count = 10
while count > 0:
    print("Guess again")
    count -= 1
else: 
    print("You've used up 10 tries")


