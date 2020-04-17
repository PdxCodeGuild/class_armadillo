import string 

alphabet = string.ascii_lowercase #import lower case letters

def rotn(text, number):
    rotn_cipher = '' #blank string
    for letter in text:  #scans over each letter in a word
        if letter in alphabet:  #this condition for input within ascii_lowercase
            rotn_cipher += alphabet[(alphabet.find(letter) + number) % 26]  #rotates the letters based on the number the user inputs
        else: #condition for characters not within ascii_lowercase
            rotn_cipher += letter
    return rotn_cipher  #creates new rotated word

text = input('Pick a word ') #prompts user for word
number = int(input('Pick a number '))   #prompts user for rotation factor
print(rotn(text, number))    