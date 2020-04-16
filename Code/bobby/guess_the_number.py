# The Guess the Number Game (My version built in my 101 course, not the one we built in the Mob Lab.).

# Import random allows the program to randomly pick a number
import random

# In my version I emplimented a difficulty selection, that allows the user
#  to select the highest number in the game i.e between 1 and 100000.
difficulty = int(input("\nchoose your dificulty! Pick a number "))
# The random.randit is what allows the program to choose a number between 1 and user choice.
computer = random.randint(1, difficulty)
# I used an open list here to be able to keep track of how many guesses the user made, upto 10
user_guesses = []
guesses = 10

# I used the While loop to track and inform the user if their guess is to high, 
# to low or correct or out of range, and also to inform the user how many guesses they used before
# guessing correctly. Along with what you enterd as guesses
while guesses > 0:
     user = input(f"\nGuess a number between 1 - {difficulty}: ")
     user = int(user)
     if user not in user_guesses:
        guesses -= 1
        user_guesses.append(user)
        
     else:
         print(f"\nYour guessed {user}, Try Again!!:")
         continue
       
     if user > difficulty or user < 1 :
        print("\nYou choice is out of range")
        continue
        # Win Message.
     if user == computer:
        print(f"\nYou Win!! It took you {10 - guesses} guesses!")
        print(f"\nYour guesses: {user_guesses}\n")
        break
      # Guiding Message.
     elif user < computer:
      print("\nToo Low...") 
     elif user > computer:
       print("\nToo High..")
    
    # Loss Message.   
else:
   print("\nSorry you ran out of Guesses  :( ")
   print(f"\nYour Guesses: {user_guesses}")