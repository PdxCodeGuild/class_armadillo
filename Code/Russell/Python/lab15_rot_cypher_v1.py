

def rot13(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_alphabet = 'nopqrstuvwxyzabcdefghijklm'

    rot_word = ''
    for letter in text:
        # using each letter from the input word, 
        # .find gives the index number from alphabet and assigns it to variable 'index'
        index = alphabet.find(letter) 
        # index number from alphabet is used to select corresponding letter from rot_alphabet
        rot_word += rot_alphabet[index] 

    return rot_word



print(rot13('vzfyrrcl'))
    

# rot_alphabet = alphabet[n:] + alphabet[:n]



