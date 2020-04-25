import random


# load words from text
def load_words(path):
    with open(path, "r") as file:
        text = file.read()
    # Turn those words into a list of words
    word_list = []
    words = text.split()
    # Only take the words longer then 5 letters
    for word in words:
        if len(word) > 5:
            word_list.append(word)

    return word_list


# calling word list function
path = 'C:/Users/talie/class_armadillo/code/talieson/data/english.txt'
hangman_words = load_words(path)


print("\n\t Welcome to hangman! Guess a letter to get started!\n")
while True:
    # generate and store the target word, create global variables
    target = random.choice(hangman_words).upper()
    guessed_letters = []
    guesses = 10
    # nested loop that enables replayability later
    while guesses > 0:
        # set the number of letters that are currently right to 0.
        correct_letters = 0
        # iterate through letters in target word.
        for letter in target:
            # if it's in guessed letters print, and iterate correct letters.
            if letter in guessed_letters:
                correct_letters += 1
                print(letter, end='')
            # if not, print a blank
            else:
                print(" _ ", end="")
        # if our correct letters counter and length of target match, win!
        if correct_letters == len(target):
            print(f'''

            Congrats! The word was {target}!
            ''')
            break

        # Main user input area.
        print(f'''
        You've guessed: {guessed_letters}
        You have {guesses} remaining!''')
        user_guess = input("\nWhat letter do you guess? ").upper().strip()

        # validate the guess is only 1 letter.
        if user_guess.isalpha() and len(user_guess) == 1:
            # check if input is in target word or previously guessed, response.
            if user_guess not in guessed_letters and user_guess not in target:
                print(f"\t Nope! No {user_guess}'s!'\n")
                guessed_letters.append(user_guess)
                guesses -= 1
            elif user_guess not in guessed_letters and user_guess in target:
                print(f"\t NICE! There is a {user_guess}!\n")
                guessed_letters.append(user_guess)
            elif user_guess in guessed_letters:
                print(f"\t You've already guessed {user_guess}!\n")
        else:
            print("\n ERROR: Please enter 1 letter!\n")
    # Check if out of guess, if so, inform the user.
    if guesses == 0:
        print(f"\t\nOh no! You're out of guesses. The word was {target}\n")
    # Check for second game.
    play_again = input("Would you like to play again? (Y/N) ").upper().strip()
    if play_again == "Y":
        continue
    if play_again == "N":
        print("Thanks for playing! Goodbye.")
        quit()
    else:
        print("Please enter a valid response.")
