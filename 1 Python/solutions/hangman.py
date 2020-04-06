
import random
import string

def get_words():
    with open('../data/english.txt') as f:
        text = f.read()

    words = text.split('\n')

    # new_list = []
    # for word in words:
    #     if len(word) > 5:
    #         new_list.append(word)
    #
    # words = new_list

    words = [word for word in words if len(word) > 5]
    return words


words = get_words()

word = random.choice(words)
print(word)
blank_word = list('_' * len(word))

guesses = 10
guessed = []
while '_' in blank_word and guesses > 0:
    print(f'You have {guesses} guess(es) left')
    print('Already guessed ' + ', '.join(guessed))
    print(' '.join(blank_word))
    letter = input('Guess a letter: ').lower()

    if len(letter) != 1 or letter not in string.ascii_lowercase:
        print('Not a letter')
        continue

    if letter in guessed:
        print('Already guessed!')
        continue

    guessed.append(letter)
    for i in range(len(word)):
        if word[i] == letter:
            blank_word[i] = word[i]
    guesses -= 1



print(f'The word was {word}')














