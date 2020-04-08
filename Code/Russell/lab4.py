import random

print('Magic 8 Ball!')

response = ['You may rely on it', 
            'Most likely', 
            'Yes', 
            'Signs point to yes', 
            'Reply hazy try again', 
            'Ask again later', 
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'My reply is no',
            'My sources say no']

input('Ask a question:')
print(random.choice(response))

try_again = input('Would you like to play again? Y/N:')
while try_again == 'Y':
    print(input('Go ahead:'))
    print(random.choice(response))
    try_again = input('Would you like to play again? Y/N:')
if try_again == 'N':
        print('Thanks for playing!')
else:
    print('Invalid response.')
   
    
            
