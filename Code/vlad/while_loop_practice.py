num = 76 # this can be any number
guess = 0
guess_limit= 5
guess_number = 0
guess = int(input(f'Guess a number 1-100:')) # guess = int(input(f'Guess a number 1-20 -1:')) by putting here -1 we counting only to 4
guess_number +=1
while guess_number < guess_limit: # while guess_number < guess_limit-1: by putting here -1 we counting only to 4
    if guess == num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} Too low - Guess again 1-100: '))
        print(f'You Win! You Guessed it {guess}')
    break # we break here if the user get it right and guess it if not then else

if guess != num:
    print(f'Sorry you lose! It was {num}')