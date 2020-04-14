import random
import time
import string


# Several lists of variables used in this program
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
eyes = ['8', '=', ':', ';']
noses = ['^', "'"]
mouths = ['P', '/', '(', ')']
time_int = 0 # how much time between the program printing each emoticon iteration
how_many_emoticons = ""

# Function #1: Returns a random face at the 'time_int' second intervals
def generate_random_emoticon():
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    random_emoticon = eye + nose + mouth

    return random_emoticon
    time.sleep(time_int)

# Function #2: Passes the user's answer [argument] to "how many emoticons" as the function's parameter. 
# Calls function #1, however many times the user requested
# parameter1 : enter an integer
def print_random_emoticon(parameter1):
    for x in range(parameter1):
        print(generate_random_emoticon())

# Function #3: Runs the function ask the user how many emoticons they want
# Prints the user's response
# Can only accept positive integers, and will continue to ask until valid response is given
def the_emoticon_game():
    is_positive = True
    how_many_emoticons = ""
    while is_positive:
        how_many_emoticons = input("How many emoticons would you like to see? ")
        if how_many_emoticons.isnumeric() and int(how_many_emoticons) > 3000:
            print(f"{how_many_emoticons}?? That is probably going to crash your terminal.")
            time.sleep(1)
            print("Consider the sweet release of a 'Ctrl + C'")
            time.sleep(3)
            print("Seriously. Kill me.")
            time.sleep(3)
            print_random_emoticon(int(how_many_emoticons))
            break
        elif how_many_emoticons.isnumeric() and int(how_many_emoticons) > 0:
            print_random_emoticon(int(how_many_emoticons))
            break
        else:
            print("I'm sorry, I don't recognize your answer.")
            time.sleep(time_int)
            print("Please enter a non-negative integer.")
            continue

# Function #4: This is the entire lab, and will allow the desperate program option to run after the program is run
def entire_lab_05():
    # Sets the initial conditions of our two While Loops
    generate_emoticon = True
    play_again = True

    while generate_emoticon:
        play_game = input("Would you like to play a game? ")
        if play_game in affirmatives:
            print("Excellent.")
            the_emoticon_game()
            break
        elif play_game in negatives:
            print("I'm sorry to hear that. Goodbye.")
            play_again = False
            break
        else:
            print("I don't understand your response. Please try again.")
            continue

    while play_again:
        second_question = input("Would you like to play again? ")
        if second_question in affirmatives:
            print("Most excellent. ")
            the_emoticon_game()
        elif second_question in negatives:
            print("I'm sorry to see you go, but thank you for testing my shitty program.")
            play_again = False
            break
        else:
            print("I don't understand your response. Please try again.")
            continue

entire_lab_05()

time.sleep(10)
print("\nIf you're still here, and you've decided you'd like to play again, ")
desperate_program = input("Press any alphabet character and 'Enter' to begin. ")

if desperate_program in string.ascii_letters:
    print("\nOh thank god. I was afraid they were going to delete me.\n")
    entire_lab_05()
else:
    print(f"\n'{desperate_program}' is not what I was hoping for...")
    print("Goodbye. ")
