

import random




person = input('Enter a person: ')

adjectives = input('Enter four adjectives, separated by comma: ').split(',')
# random.shuffle(adjectives)
# adjective1 = adjectives[0]
# adjective2 = adjectives[1]

adjective1 = random.choice(adjectives)
adjective2 = random.choice(adjectives)

noun1, noun2 = input('Enter two nouns, separated by comma: ').split(',')
verb1, verb2 = input('Enter two verbs, separated by comma: ').split(',')
madlib = f"I believe that [{person}]’s views were the most [{adjective1}] of all the [{adjective2}] men in our time. We should strive to do things in his [{noun1}]: not to use [{verb1}] in fighting for our cause, but by [{verb2}] in anything you believe is [{noun2}]."
print(madlib)

