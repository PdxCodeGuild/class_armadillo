'''Write a program that prompts the user for a string, and encodes it 
with ROT13. For each character, find the corresponding character, add 
it to an output string. Notice that there are 26 letters in the English
 language, so encryption is the same as decryption.'''

# defines the actual ROT function.
def rot13(phrase):
# creates the string code will iterate over to find the indices.
    abc = 'abcdefghijklmnopqrstuvwxyz'
# creates an open string the user phrase that will be entered later in the code.
    user_phrase = ''
# initiates the loop        
    for char in phrase:
# places a space between words in the string.       
        if char == ' ':
            user_phrase += ' ' 
# attaches the user phrase to the new indices using the rot13 code. 
        else:
            user_phrase += abc[(abc.find(char)+13)%26]
# returns the user phrase from below.            
    return user_phrase
# has the user input what they would like encrypted.
phrase = input('Enter the phrase you would like to have encrypted. ')
# prints the encrypted input.
print(f'Your encrypted code is {rot13(phrase)}')
