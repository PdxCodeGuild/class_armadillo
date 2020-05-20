import random

computer = random.choice(range(10))

user = input('Try and guess the correct number between 1 and 10!: ')
user = int(user)


if user == computer:
    print('You got it!')
   
elif user < computer: 
    print('Too Low!')
    
elif user > computer:
    print('Too High!')

print('The number was:', computer)

play_again = ''
while True:
    play_again == input('Play again Y/N:')
    if play_again == 'N':
        print('Thanks for playing')
        break
    guess = int(input('Enter number:'))
    computer = random.choice(range(10))
    
    print(f'The number was: {computer}')
    if guess == computer:
        print('You got it!')
   
    elif guess < computer: 
        print('Too Low!')
    
    elif guess > computer:
        print('Too High!') 
