# Lab 8 Magic 8 Ball
# Troy Fitzgerald

# imports modules.
import random
import time

# creates a list for the Magic 8 Ball to choose from.
answers = ['Reply hazy try again', 'Yes', 'My sources say no', 'Without a doubt', 'Hell Nah!', 'Hell Yeah!', 
'Concentrate and ask again', 'Lookin good', 'Not so fast my friend', 'Not a chance']
# statement for intro.
print('Hello there random stranger on the street.')
# statement gauging interest to ask question.
print('Can I interest you in asking the Magic 8 Ball some questions and predict your future?')
# tells the user to answer if they want to play.
user_choice = input('Enter "y" for yes and "n" for no: ')
# tests the user's answer against the user's choice to begin or end game.
if user_choice in ['y' or 'yes']:
    print('Awesome, here we go.')
elif user_choice in ['n' or 'no']:
    print('Get outta here...who needs ya!')
    quit()
else:
    print(' I did not understand. Please reply again.')
# defines the function.
def magic_8_ball():
    # asks the use what they are asking.
    print('What is your question?')
    # user question to be predeicted.
    user_question = input('')
    # answer to be generated from list of answers.
    answer = random.choice(answers)
    # prints the 8 ball answer.
    print(answer)
    # gives dramatic pause before asking if user wants to ask anotehr question. 
    time.sleep(2)
    # runs ask_me_more function to ask more questions.
    ask_me_more()

# defines the function.
def ask_me_more():
    # asks if user would like to ask another question.
    user_choice = input("Would you like to ask another question? ") 
    # tests the user's answer against the user's choice to begin or end game.    
    if user_choice in ['y' or 'yes']:
        print('Awesome, here we go again.')
        magic_8_ball()
    elif user_choice in ['n' or 'no']:
        print('Why not? Don\'t like what you hear!!')
        quit()
    else:
        print(' I did not understand. Please reply again.')
        # recalls the function.
        ask_me_more()
# runs the function.    
magic_8_ball()
