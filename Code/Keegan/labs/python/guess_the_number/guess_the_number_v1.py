import random  # get that random module

def mind_reader():
    pass

# generate a random integer between 1 and 10
secret = random.randint(1, 10)  

number_of_guesses = 0
while number_of_guesses < 10:
    # print(f"{number_of_guesses = }") # brand new syntax in Python 3.8 to print a label with a variable in an f-string

    print(f"Guesses remaining: {10 - number_of_guesses}")

    # prompt the user for a guess
    guess = input("Please enter a number between 1 and 10: ")

    # convert the guess string into an integer
    guess = int(guess)

    # test the guess against the secret
    if guess > secret:
        print("Too high!")

    elif guess < secret:
        print("Too low!")

    elif guess == secret:
        if number_of_guesses <= 1:
            message = f"You're a wizard, Harry!"
        elif number_of_guesses <= 4:
            message = f"You're above average!"
        elif number_of_guesses <= 8:
            message = f"You're below average!"
        else:
            message = f"You statistically suck, kid!"
        
        print(message)    
        print(f"You guessed the secret in {number_of_guesses + 1} guess(es)!")
        break

    number_of_guesses += 1
