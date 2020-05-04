#Lab 15:ROT 13 Version 1
 
#imports module
import string

def rot13(text):
    alpha_shift = 'nopqrstuvwxyzabcdefghijklm' #alphabet shifted 13 places
    alpha = string.ascii_lowercase  

#String that Rot13 word will be appended to
    rot_num = ''

    #Looping through each character
    for char in text:
        #finds the exact index and shows the new letter
        index = alpha.find(char)
        rot_num += alpha_shift[index]  
    return rot_num  #returns the value

#Asks the user for a word to be encrypted
word = input('Type in a word to be encrypted. ')

#prints encrypted word
print(f'Your encrypted code is {rot13(word)}')

#Random strings with ROT 13 encryption
print(rot13('quarantine'))
print(rot13('hello world!'))
