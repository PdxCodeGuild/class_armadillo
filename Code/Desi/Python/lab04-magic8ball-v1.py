# Lab 04


import random

# Print a welcome screen to the user.
welcome_screen = ("Welcome to the Magic 8 Ball")

# Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
user = input("Will the quarantine be lifted soon? ")


possible_random_questions = ["without a doubt", "ask again later", "not likely", 
"do you like to suffer", "sooner rather than later", "not this year", "I thought you enjoyed being on lockdown"]


#Use the random module's `random.choice()` to choose a prediction.
random.choice(possible_random_questions)


# print("random item from list is: ", random.choice(numberList))
print(random.choice(possible_random_questions))




# import random

# numberList = [111,222,333,444,555]
# print("random item from list is: ", random.choice(numberList))