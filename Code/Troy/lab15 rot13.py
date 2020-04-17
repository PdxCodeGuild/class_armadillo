'''Write a program that prompts the user for a string, and encodes it 
with ROT13. For each character, find the corresponding character, add 
it to an output string. Notice that there are 26 letters in the English
 language, so encryption is the same as decryption.'''

import string

def rot13(phrase):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    user_phrase = ''
       
    for char in phrase:
        if char == ' ':
            user_phrase += ' ' 
        else:
            user_phrase += abc[(abc.find(char)+13)%26]
    return user_phrase

phrase = 'hello world'

print(rot13(phrase))
#print(rot13(rot13(phrase)))