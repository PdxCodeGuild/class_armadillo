import random

run = True
while True:

    print("Who dares disturb the Magic 8 balls slumber!?")
    question = input("Ask your question mortal.. If you dare! ")

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

    print(answer)
    run = False

    while not run:

        replay = input("Do you dare ask again!? (Y/N) ")

        if replay == 'Y':
            run = True
            break
        elif replay == 'N':
            print("Your fate is in your hands now mortal...")
            exit()
        else:
            print("Do not play games with fate!")
