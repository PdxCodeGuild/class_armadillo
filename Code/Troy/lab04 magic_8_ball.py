''' Instructions
Let's write a program to simulate the classic "Magic Eight Ball"

Print a welcome screen to the user.
Prompt the user to ask the 8-ball a question.
For example: "Will I win the lottery tomorrow?"
Use the random module's random.choice() to choose a prediction.
Display the result of the prediction.'''

# imports the random and time module.
import random
import time

# creates a list for the Magic 8 Ball to choose from.
answers = ["Reply hazy try again", "Yes", "My sources say no", "Without a doubt", "Hell Nah!", "Hell Yeah!", 
"Concentrate and ask again", "Lookin good", "Not so fast my friend", "Not a chance"]
# statement for intro.
print("Hello there random stranger on the street.")
# statement to ask the person if they wish to ask the Magic 8 Ball questions.
print("Can I interest you in asking the Magic 8 Ball some questions and predict your future?")
# chooses the user's answer to play
user_choice = input("Enter 'y' for yes and 'n' for no: ")
# tests the user's answer against the user's choice to begin or end game.
if user_choice == 'y' or 'yes':
    print("Awesome, here we go. Ask your question. ")

elif user_choice == 'n' or 'no':
    print("Get outta here...who needs ya!")

user_question = input("")
# generates a random answer from the answers list and prints it.
answer = random.choice(answers)
print(answer)
# gives dramatic pause to game before continuing.
time.sleep(2)
# asks the user if they would like to play again.
user_choice = input("Would you like to play again? ")
# tests the user's answer against the user's choice to continue the game.
if user_choice == 'y':
    print("Awesome, ask another question. ")
# lets the user input the desired question.
    user_question = input("")
 # generates a random answer from the answers list and prints it.    
    answer = random.choice(answers)
    print(answer)  
# ends the game based on user answer.
else:
    print("Get outta here...who needs ya!")

