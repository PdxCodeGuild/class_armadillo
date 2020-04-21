# 4/20/2020
# Strings practice

# Problem 1
def double_letters(word):
    '''
    Get a string from the user, 
    print out another string, doubling every letter.
    '''
    # create an empty variable to 
    # hold the doubled word
    doubled_word = ''

    # iterate through each letter
    for letter in word:
        letter *= 2  # double the letter
        doubled_word += letter # add doubled letter to new word

    # return doubled_word

# word = input("Enter a word to double each letter: ")
word = "hello"
double_letters(word)

def missing_char(word):
    '''
    takes a string, and returns a list of strings, 
    each missing a different character.
    '''
    # create an empty list to hold word copies
    word_list = []

    # loop through each letter in the word
    for index in range(1, len(word) + 1):
    # create a copy of the word minus that letter

        # slice the word into two parts
                   #word[start:end]
        left_part = word[0:index - 1]
        right_part = word[index:len(word)]

        # combine the two parts
        new_word = left_part + right_part

        word_list.append(new_word)  # add each word to the list

    return word_list


    # add the copy of the word to a list

word = 'kitten'
print(missing_char(word))