''' Instructions
Let's write a program to simulate the classic "Magic Eight Ball"

Print a welcome screen to the user.
Prompt the user to ask the 8-ball a question.
For example: "Will I win the lottery tomorrow?"
Use the random module's random.choice() to choose a prediction.
Display the result of the prediction.'''

import random
import time

answers = ["Reply hazy try again", "Yes", "My sources say no", "Without a doubt", "Hell Nah!", "Hell Yeah!", 
"Concentrate and ask again", "Lookin good", "Not so fast my friend", "Not a chance"]

print("Hello there random stranger on the street.")

print("Can I interest you in asking the Magic 8 Ball some questions and predict your future?")

user_choice = input("Enter 'y' for yes and 'n' for no: ")

if user_choice == 'y':
    print("Awesome, here we go. Ask your question. ")

elif user_choice == 'n':
    print("Get outta here...who needs ya!")

user_question = input("")

answer = random.choice(answers)
print(answer)

time.sleep(2)


while user_choice == 'y':
    print("Awesome, ask your question. ")
    
    user_question = input("")
    
    answer = random.choice(answers)
    print(answer)  

    user_choice = input("Would you like to play again? ")

else:
    print("Get outta here...who needs ya!")





