#Lab 4 Magic 8-Ball
#4/7/2020

import random

#Print a welcome screen to the user
print("Welcome to Magic 8-Ball!!")

#Prompt the user to ask the 8-ball a question
question = input('Ask the 8-Ball anything you\'d like. ' )

#Use random module to choose a prediction and display the result
result = ['Nope', 'Yes, definitely', 'You don\'t stand a chance', 'Maybe', 'My sources say no', 'Ask again later', 'Most likely']
predictions = random.choice(result)
print(predictions)


# #Keep asking the user for a question
ques_cont = input('Would you like to ask another question? If not type "done". ')
while ques_cont == 'yes':
    question = input('Ask the 8-Ball anything you\'d like. ' )
    print(predictions)
    ques_cont = input('Would you like to ask another question? If not type "done". ')
if ques_cont == 'done':
    print('Have a good day!')