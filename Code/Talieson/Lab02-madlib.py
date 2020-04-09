import shlex
import random

# Run ensures the game runs and allows for repeat games after it finishes
run = True
checkIn = False

# Main play loop
while run:

    # Check if they want a random game.
    randomGame = input("Do you want to play a random game? (if so, input Y. "
                       "If Y, you won't be able to pick the words)")

    # If the game has been set to random, use a random option from the lists.
    if randomGame == 'Y':

        randBodyPart = ('nose', 'leg', 'kneecap', 'eye', 'wrists', 'eyebrow',
                        'fingernails')
        randLargeThing = ('Eifel Tower', 'Sun', 'Madagascar',
                          'Zues, God of STORMS!',
                          'The Blue Guy from the Watchmen')
        randItemAdj = ('exceptional', 'shiny', '+3 flaming', 'glowing',
                       'simple')
        randItem = ('frisbee', 'fishguts', 'masks', 'knight', 'drumkit')
        randCreationProcess = ('brewing', 'molding', 'knitting', 'carving')
        randItems = ('quarters', 'locks', 'buckets', 'squirels', 'globes')
        randTool = ('hoe', 'axe', 'basket', 'lightsaber')
        randComplicatedSubject = ('Quantum Mechanics', 'Engineering',
                                  'The Art of the Deal', 'Interpretive Dance')
        randAdjective = ('moist', 'ambitious', 'moxy-iful',
                         'cybernetically engineered')

        bodypart = random.choice(randBodyPart)
        largeThing = random.choice(randLargeThing)
        itemAdj = random.choice(randItemAdj)
        item = random.choice(randItem)
        creationProcess = random.choice(randCreationProcess)
        items = random.choice(randItems)
        tool = random.choice(randTool)
        complicatedSubject = random.choice(randComplicatedSubject)
        adjective = random.choice(randAdjective)

    else:
        answers = input("enter the following things, seperated by a space: a "
                        "bodypart (G rated please), a very large proper noun, "
                        "an adjective that describes an object, any item at "
                        "all, a method of creating something, objects(plural)"
                        ", a tool, an advanced field of study, and any"
                        "adjective.")

        # Take the input from answers and split into a list of strings.
        answersKey = shlex.split(answers)

        bodypart = answersKey[0]
        largeThing = answersKey[1]
        itemAdj = answersKey[2]
        item = answersKey[3]
        creationProcess = answersKey[4]
        items = answersKey[5]
        tool = answersKey[6]
        complicatedSubject = answersKey[7]
        adjective = answersKey[8]

    print(f"Egyptian men and women wore makeup. It was thought to have healing"
          "powers, it helped protect their {bodypart} from (the) {largeThing}."
          "They used {itemAdj} {item} to help with infections. They were one "
          "of the first civilizations to invent writing. They  also used ink "
          "to write and paper called papyrus. The Ancient Egyptians were "
          "scientists and mathematicians. They had numerous inventions "
          "including ways to {creationProcess} {items}, medicine, cosmetics,"
          "the calendar, the {tool} for farming, musical instruments, and even"
          "{complicatedSubject}. They were truly a(n) {adjective} people.")

    # We're done playing. End this run and ask if they'd like to try again.
    run = False
    checkIn = True
    # Loop to check for a second game.
    while checkIn:
        checkIn = False
        again = str(input("That was SO silly! play again? (Y/N)"))
        if again != "Y":
            run = True
        elif again != "N":
            print("Thanks for playing!")
            break
        else:
            print("I'm sorry, that's not a valid response.")
            checkIn = True
