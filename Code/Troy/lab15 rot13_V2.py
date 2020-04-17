'''Version 2
Allow the user to input the amount of rotation used in the 
encryption. (ROTN)'''

def rot(phrase, n):

    abc = 'abcdefghijklmnopqrstuvwxyz'
    user_phrase = ''
    
    for char in phrase:
        if char == ' ':
                user_phrase += ' '
        index = abc.find(char)
       
        index += n

        while index >= len(abc):
            index -= len(abc)
            
        user_phrase += abc[index]

    return user_phrase

phrase = input('Phrase you want encrypted. ')
n = int(input('Enter the rotational number. '))

print(f'Your new code is {rot(phrase, n)}')

