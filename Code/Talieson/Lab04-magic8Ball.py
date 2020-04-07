import random

# Run is used to determine if a new game is to be played.
run = True
# Determines if the Magic 8 ball has alraedy introduced himself or not.
intro = False

# Main game loop, gives his original intro if he hasn't yet
while True:
    if not intro:
        print("Who dares disturb the Magic 8 balls slumber!?")
        question = input("Ask your question mortal.. If you dare! ")
# If he's introduced himself, he isn't going to again, his time is valuable
    else:
        question = input("Fine! What is your next question? ")

    answers = ("It is certain, the tea leaves couldn't be clearer.",
               "Of course! I just knew that off the top of my head.",
               "I've seen it in the winds, it shall be so!",
               "You may rely on it.",
               "I've cast the bones, they point to yes!",
               "Reply hazy try again..",
               "The storms obscure the stars, check back when they clear..",
               "I've misplaced my Tarot cards.. maybe ask later. IF YOU DARE.",
               "The omens are ill.",
               "There is no hope in any timeline I've witnessed.",
               "The blood is black, this shall not be so.",
               "Hahaha! Nay, of course nay.. are ye mad?!")

    answer = random.choice(answers)
# Returns the answer and makes run false, prompting check for second game
    print(answer)
    run = False

    while not run:

        replay = input("Do you dare ask again!? (Y/N) ")

        if replay == 'Y':
            run = True
            intro = True
            break
        elif replay == 'N':
            print("Your fate is in your hands now mortal...")
            exit()
        else:
            print("Do not play games with fate!")
