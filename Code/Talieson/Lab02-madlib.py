import shlex
import random

# Run ensures the game runs and allows for repeat games after it finishes
run = True
check_in = False

# Main play loop
while run:
    # Check if they want a random game.
    random_game = input('''Do you want to play a random game? (if so, input Y.
                        If Y, you won't be able to pick the words) ''')

    # If the game has been set to random, use a random option from the lists.
    if random_game == 'Y':

        random_body_part = ('nose', 'leg', 'kneecap', 'eye', 'wrists',
                            'eyebrow', 'fingernails')
        random_large_thing = ('Eifel Tower', 'Sun', 'Madagascar',
                              'Zues, God of STORMS!',
                              'The Blue Guy from the Watchmen')
        random_item_adj = ('exceptional', 'shiny', '+3 flaming', 'glowing',
                           'simple')
        random_item = ('frisbee', 'fishguts', 'masks', 'knight', 'drumkit')
        random_creation_process = ('brewing', 'molding', 'knitting', 'carving')
        random_items = ('quarters', 'locks', 'buckets', 'squirels', 'globes')
        random_tool = ('hoe', 'axe', 'basket', 'lightsaber')
        random_complicated_subject = ('Quantum Mechanics', 'Engineering',
                                      'The Art of the Deal',
                                      'Interpretive Dance')
        random_adjective = ('moist', 'ambitious', 'moxy-iful',
                            'cybernetically engineered')

        bodypart = random.choice(random_body_part)
        large_thing = random.choice(random_large_thing)
        item_adj = random.choice(random_item_adj)
        item = random.choice(random_item)
        creation_process = random.choice(random_creation_process)
        items = random.choice(random_items)
        tool = random.choice(random_tool)
        complicated_subject = random.choice(random_complicated_subject)
        adjective = random.choice(random_adjective)

    else:
        answers = input('''enter the following things, seperated by a ", ": a
                         bodypart (G rated please), a very large proper noun,
                         an adjective that describes an object, any item at
                         all, a method of creating something, objects(plural)
                        , a tool, an advanced field of study, and any
                        adjective.''')

        # Take the input from answers and split into a list of strings.
        answer_key = shlex.split(answers)
        bodypart = answer_key[0]
        large_thing = answer_key[1]
        item_adj = answer_key[2]
        item = answer_key[3]
        creation_process = answer_key[4]
        items = answer_key[5]
        tool = answer_key[6]
        complicated_subject = answer_key[7]
        adjective = answer_key[8]

    print(f'''
    Egyptian men and women wore makeup. It was thought to have healing
    powers, it helped protect their {bodypart} from (the) {large_thing}
    They used {item_adj} {item} to help with infections. They were one
    of the first civilizations to invent writing. They  also used ink
    to write and paper called papyrus. The Ancient Egyptians were
    scientists and mathematicians. They had numerous inventions
    including ways to {creation_process} {items}, medicine, cosmetics
    the calendar, the {tool} for farming, musical instruments, and even
    {complicated_subject}. They were truly a(n) {adjective} people.''')

    # We're done playing. End this run and ask if they'd like to try again.
    run = False
    checkIn = True
    # Loop to check for a second game.
    while checkIn:
        checkIn = False
        again = str(input("That was SO silly! play again? (Y/N)"))
        if again == "Y":
            run = True
            break
        elif again == "N":
            print("Thanks for playing!")
            exit()
        else:
            print("I'm sorry, that's not a valid response.")
            checkIn = True
