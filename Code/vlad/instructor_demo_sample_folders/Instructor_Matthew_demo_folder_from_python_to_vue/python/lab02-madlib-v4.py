



keep_running = 'yes'
while keep_running == 'yes':
    person = input('Enter a person: ')
    adjective1 = input('Enter an adjective: ')
    adjective2 = input('Enter an adjective: ')
    noun1 = input('Enter a noun: ')
    noun2 = input('Enter a noun: ')
    verb1 = input('Enter a verb: ')
    verb2 = input('Enter a verb: ')

    madlib = f"I believe that {person}’s views were the most {adjective1} of all the {adjective2} men in our time. We should strive to do things in his {noun1}: not to use {verb1} in fighting for our cause, but by {verb2} in anything you believe is {noun2}."
    print(madlib)

    while True:
        keep_running = input('Would you like to play again? yes/no ')
        if keep_running == 'yes' or keep_running == 'no':
            break
        print('response not recognized')
    


