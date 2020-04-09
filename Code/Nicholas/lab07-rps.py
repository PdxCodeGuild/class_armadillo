import random
#loops back here
play_again = True
while play_again:
    #gets user input, then generates computer's output 
    user = input('Choose rock, paper, or scissors: ').lower() #allows user to enter any input without being case sensitive
    choices = ['rock' , 'paper', 'scissors']
    computer = random.choice(choices)

    # paper vs paper (tie)
    # scissors vs scissors (tie)
    # rock vs rock (tie)
    if user == computer:
        print(f'Computer chose {computer}! That is a tie!')
    # rock vs paper
    elif user == 'rock' and computer =='paper':
        print('Computer Wins!')   
    # rock vs scissors
    elif user == 'rock' and computer =='scissors':
        print('You Win!')
    # paper vs rock
    elif user == 'paper' and computer == 'rock':
        print('You Win!')
    # paper vs scissors
    elif user == 'paper' and computer == 'scissors':
        print('Computer Wins!')
    # scissors vs rock
    elif user == 'scissors' and computer == 'rock':
        print('Computer Wins!')
    # scissors vs paper
    elif user == 'scissors' and user == 'paper':
        print('You Win!')
    else:
        print('That is not a valid entry')#generates if anything but rock, paper, or scissors entered    

    another_round = input("Wanna play again? Y/N ").upper()
    if another_round == "N":
        print("See ya later!")
        break        