# Problem 1
# Get a string from the user, print out another string, doubling every letter.
def double_letters(word):
    double_letters = ''
    # for i in range(0,-1,1):
    #     double_letters += word[i]
    for i in word:
        print(i*2, end="")
    return double_letters

# print(double_letters('hello')) # hheelllloo

# Problem 2
# Write a function that takes a string, and returns a list of strings, each missing a different character.
def missing_char(word):
    list1 = []
    # word = list(word)
    for i in range(len(word)):
        list1.append(list(word))
    
    increment = 0

    for word in list1:
        word = word.pop(increment)
        increment += 1

    for word in list1:
        print(''.join(word), end=' ')



missing_char('kitten') # ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

# Problem 3
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
  ...
# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v

# Problem 4
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
  ...
# print(count_hi('hihi')) # 2
# Problem 5
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

def cat_dog(text):
  ...
# print(cat_dog('catdog')) # True
# print(cat_dog('catcat')) # False
# print(cat_dog('catdogcatdog')) # True

# Problem 6
# Return the number of letter occurances in a string.

def count_letter(letter, word):
    ...
# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2

# Problem 7
# Convert input strings to lowercase without any surrounding whitespace.

def lower_case(text):
  ...
# print(lower_case("SUPER!")) # 'super!'
# print(lower_case("        NANNANANANA BATMAN        ")) # 'nannananana batman'