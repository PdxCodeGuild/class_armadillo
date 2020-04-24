import random
# write function to load words from .txt
def load_words(path):

    with open(path, 'r') as f:
        words = f.read()
    list_of_words = words.split()
    
    list_of_long_words = []
    for word in list_of_words:
        if len(word) > 5:
            list_of_long_words.append(word)
    return list_of_long_words

path = '../../../1 Python/data/english.txt'

hangman_words = load_words(path)

random_word = random.choice(hangman_words)
guesses = 10
already_guessed = []
print(random_word)

while guesses > 0:
    for letter in random_word:
        if letter in already_guessed:
            print(f'{letter} ', end='')
        else:
            print('_ ', end='')
    print()
    print(f"# of guesses remaining: {guesses}")
    
    user_guess = input("Guess a letter: ")
    if user_guess in random_word:
        print('good job')
        already_guessed.append(user_guess)

        # guesses += 1 # guesses = guesses + 1

    if user_guess in already_guessed:
        print(f"You have already guessed {user_guess}")
    else:
        already_guessed.append(user_guess)
        guesses -= 1 # guesses = guesses - 1
    print(already_guessed)
    print()
    # break



# print(random_word)
# print(hangman_words)