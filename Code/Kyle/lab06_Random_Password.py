# Lab 6: Random Password Generator Version 1-3
# Kyle Harasimowicz

# Let's generate a password of length n using a while loop and random.choice, 
# this will be a string of random characters, e.g. a62xB95. 
# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

import random
import string
import secrets
import time

time_int = 1
int1 = ""

letters = string.ascii_letters
numbers = string.digits
special_characters = "!@#$%^&*?"
all_characters = string.ascii_letters + string.digits + special_characters
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
user_length = ""
user_generated_password = ""
password = ""
loop_1 = True
loop_2 = True
loop_3 = True
seraph_word_list = ["seraph", "choice", "random", "first", "user", "specific", "created", "second", "1st", "2nd"]
seraph_word_list_first = ["seraph", "choice", "random", "first", "1st"]
seraph_word_list_second = ["user", "created", "specific", "second", "2nd"]


# Generates a secure, random password. Length is randomized between 32 and 64 characters
# Characters are all upper/lowercase letters, all digits, and commonly accepted special characters
def generate_random_password():
    int1 = int(random.randint(32, 65))
    password = ''.join(secrets.choice(all_characters) for i in range(int1))
    print(password)
    time.sleep(time_int)

# Securely shuffles a previously-generated password
def shake_and_bake():
    shuffled_password = list(user_generated_password)
    secrets.SystemRandom().shuffle(shuffled_password)
    user_generated_password = ''.join(shuffled_password)
    print ("Secure Password is ", user_generated_password)

# Allows user to create a secure password. User selects the length, and numerical composition of
# letters, numbers, and special characters
def generate_user_password_inputs():
    # begin the mega-loop to create a password using user-generated responses
    create_a_user_given_password = True
    while create_a_user_given_password:
        # begin the first loop - set the length of the password
        within_range = True
        user_total_length = "" # Contains the initial question (How many characters?) and the loops answer (X# Characters)
        while within_range:
            user_total_length = input("How many characters do you want your password to be? Choose a number between 32 and 64: ")
            if user_total_length.isnumeric() and int(user_total_length) >= 32 and int(user_total_length) <= 64:
                break  # user has successfully entered a length between 32 and 64 characters. Kicks us out to the next step
            else:
                print("I'm sorry, I don't recognize your answer.")
                time.sleep(time_int)
                print("Please enter an integer between 32 and 64")
                continue

        # begin the second loop. Ask how many characters in the password are made of letters.
        how_many_letters = True
        user_letters = ""   #Contains the second question (How many of the total characters are letters?),
                            # and contains the answer (Y letters of X Characters)
        while how_many_letters:
            # in this question, we ask the user to limit the number of letters
            # to be within the total number of characters in their first answer
            user_letters = input("How many characters do you want to be letters? Choose a number between 1 and " + user_total_length + ": ")
            if user_letters.isnumeric() and int(user_letters) >= 1 and int(user_letters) <= int(user_total_length):
                # takes the amount of letters the user requests, and adds a random selection to the eventual user password.
                user_generated_password = ''.join(secrets.choice(all_characters) for i in range(int(user_letters)))
                # break # if the user answer meets the parameters, we kick out of this loop
                break 
            else:
                print("I'm sorry, I don't recognize your answer.")
                time.sleep(time_int)
                print("Please enter a non-negative integer between 1 and " + user_total_length)
                continue

        # begin the third loop. Ask how many characters in the password are made of numbers.
        how_many_numbers = True
        user_numbers = ""   # Contains the third question (How many of the remaining characters do you want to be digits?)
                            # and passes the answer (Z Digits of (X - Y))
        while how_many_numbers:
            # in this question, we're asking how many of the remaining characters does the user want to be digits
            # user_numbers >= 0 and user_numbers <= user_total_length - user_letters
            user_numbers = input("How many characters do you want to be numbers? Choose a number between 0 and " + str((int(user_total_length) - int(user_letters))) + ": ")
            if user_numbers.isnumeric() and int(user_numbers) >= 0 and int(user_numbers) <= (int(user_total_length) - int(user_letters)):
                # takes the amount of numbers requested, and adds it to the letters already in the user generated password
                user_generated_password += ''.join(secrets.choice(numbers) for i in range(int(user_numbers)))
                break #the user has successfully entered a number in the given parameters. On to the last loop.
            else:
                print("I'm sorry, I don't recognize your answer.")
                time.sleep(time_int)
                print("Please enter a non-negative integer between 0 and " + str((int(user_letters) - int(user_total_length))))
                continue

        # Generate the number of special characters to be used.
        # This is only the remaing space available: Special = (Total - Letters - Numbers)
        user_total_specials = int(user_total_length) - int(user_letters) - int(user_numbers)

        #adds the final amount of characters to the user password; the number of special characters
        user_generated_password += ''.join(secrets.choice(special_characters) for i in range(int(user_total_specials)))

        print("Okay, I'm about to generate you a random password.")
        print(f"Your password is {user_total_length} characters long, and contains: ")
        print(f"{user_letters} letters, {user_numbers} numbers, and {user_total_specials} special characters. \n")
        
        are_you_satisfied = True
        send_it = ""
        while are_you_satisfied:
            send_it = input("Are you satisfied with your parameters? ")
            if send_it in affirmatives:
                print("Excellent. \n")
                create_a_user_given_password = False
                break
            elif send_it in negatives:
                print("That's unfortunate, but my human overlord is tired of debugging this program.")
                print("I don't have any other options. Please answer the next question affirmatively.")
                print("If you no longer wish to generate a password, enter 'CTRL + C' at any time to end this program.")
                time.sleep(1)
                continue
 
    
    print("One last step to ensure maximum security for your password.")
    time.sleep(time_int)
    print("I've run a secure algorithm to generate each of your requested character types.") 
    time.sleep(time_int)
    print("Last step: Shake and Bake.")

    shuffled_password = list(user_generated_password)
    secrets.SystemRandom().shuffle(shuffled_password)
    user_generated_password = ''.join(shuffled_password)
    print ("Secure Password is ", user_generated_password)

# Program introduces itself, gives the user options to create a password of their own
# or receive a randomly generated password
def seraphs_choice():
    initial_question = True
    while initial_question:
        print("\nSeraph's Choice - Entirely Random ")
        time.sleep(time_int)
        print("User Created - I'll solicit your input for the specific number and type of characters. ")
        time.sleep(time_int)
        while True:
            user_response_question_1 = input("Choose: ").lower()
            if user_response_question_1 in seraph_word_list:
                False
                initial_question = False
                break
            else:
                print("I'm sorry, I don't recognize that answer. ")
                print("Choose either the first or the second option.")
                continue

    while loop_2:
        if user_response_question_1 in seraph_word_list_first:
            print("(processing...)")
            time.sleep(time_int * 3)
            print("Your new secure password is: \n")
            time.sleep(time_int)
            generate_random_password()
            print("\n")
            break
        elif user_response_question_1 in seraph_word_list_second:
            print("Then...let us begin.")
            time.sleep(time_int)
            generate_user_password_inputs()
            time.sleep(time_int)
            break

print("Hello, user. My name is Seraph, and I'm a program designed to help you create a secure password.")
time.sleep(time_int)
print("Would you like me to create an entirely random password for you?")
time.sleep(time_int)
print("Or would you like to help create your own secure password?")
time.sleep(time_int)

seraphs_choice()

# Infinite loop
# infinite_loop = True
while True:
    play_again = input("Would you like to generate another password? ")
    if play_again in affirmatives:
        print("Certainly.")
        time.sleep(time_int)
        print("Would you like me to create an entirely random password for you?")
        time.sleep(time_int)
        print("Or would you like to help create your own secure password this time?")
        seraphs_choice()
        continue
    elif play_again in negatives:
        print("Thank you for playing. Goodbye.")
        False
        break
    else:
        print("I don't understand your response. Please respond affirmatively or negatively.")
        continue

    