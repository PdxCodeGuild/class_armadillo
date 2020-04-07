import shlex

# Run ensures the game runs and allows for repeat games after it finishes
run = True
checkIn = False

# Main play loop
while run:

    answers = input('enter the following things, seperated by a space: A bodypart (G rated please), a very large proper noun, an adjective that describes an object, any item at all, a method of creating something, objects(plural), a tool, an advanced field of study, and any adjective.')
    
    # Take the input from answers and split it into a list of multiple strings
    answersKey = shlex.split(answers)

    bodypart = answersKey[0]
    largeThing = answersKey[1]
    itemAdj = answersKey[2]
    item = answersKey[3]
    creationProcess = answersKey[4]
    items = answersKey[5]
    tool =answersKey[6]
    complicatedSubject = answersKey[7]
    adjective = answersKey[8]

    print(f' Egyptian men and women wore makeup. It was thought to have healing powers, plus it helped protect their {bodypart} from the {largeThing}. They used {itemAdj} {item} to help with infections. They were one of the first civilizations to invent writing. They also used ink to write and paper called papyrus. The Ancient Egyptians were scientists and mathematicians. They had numerous inventions including ways to {creationProcess} {items}, medicine, cosmetics, the calendar, the {tool} for farming, musical instruments, and even {complicatedSubject}. They were truly a(n) {adjective} people.')

    # We're done playing. End this run and ask if they'd like to try again.
    run = False
    checkIn = True
    
    # Loop to check for a second game.
    while checkIn:
        checkIn = False
        again=str(input("That was SO silly! Do you want to play again? (type yes or no)"))
        if again == "no":
            print ("Thanks for playing!")
            break
        elif again == "yes":
            run = True
        else:
            print("I'm sorry that's not a valid response.")
            checkIn = True
        