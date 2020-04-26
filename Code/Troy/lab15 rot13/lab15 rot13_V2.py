# Lab 15 ROT 13
# Troy Fitzgerald


'''Version 2
Allow the user to input the amount of rotation used in the 
encryption. (ROTN)'''

# defines the actual ROT function.
def rot(phrase, n):
    # creates the string code will iterate over to find the indices.
    abc = 'abcdefghijklmnopqrstuvwxyz'
    # creates an open string the user phrase that will be entered later in the code.   
    user_phrase = ''
    # initiates the loop   
    for char in phrase:
        # places a space between words in the string.        
        if char == ' ':
                user_phrase += ' '
        # sets the index to correlate the letter to the indices.                
        index = abc.find(char)
        # adds how many indices to moved from the original indices spot..      
        index += n
        # while loop loops over the length of alphabet.
        while index >= len(abc):
            index -= len(abc)
            
        user_phrase += abc[index]
    # returns the user phrase from below.
    return user_phrase
# has the user input what they would like encrypted and the rotational value..
phrase = input('Phrase you want encrypted. ')
n = int(input('Enter the rotational number. '))
# prints the encrypted input.
print(f'Your new code is {rot(phrase, n)}')

