

def rotn(text, n):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # create a rot alphabet with slice notation
    # user input n as first index, then adding the remaining letters before n
    rot_alphabet = alphabet[n:] + alphabet[:n] 

    rot_word = '' # initiate rot word with blank string
    for char in text:
        index = alphabet.find(char) 
        # index number from alphabet is used to select corresponding letter from rot_alphabet
        rot_char = rot_alphabet[index] 
        rot_word += rot_char # for each iteration, the rot character is added to rot word string 

    return rot_word

print(rotn('Russell', 12)) 
print(rotn('hello', 2)) # jgnnq
print(rotn('jgnnq', -2)) # hello