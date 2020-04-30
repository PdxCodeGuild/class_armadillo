#lab02-madlib-v2 instructor sample: 

# how much can we put on one line?

# age = input('enter your age: ')
# age = int(age)

# age = int(input('enter your age: '))



# person = input('Enter a person: ')
# adjectives = input('Enter two adjectives, separated by comma: ')  # fluffy,coarse
# adjectives = adjectives.split(',')
# adjective1 = adjectives[0]
# adjective2 = adjectives[1]

# fancy way to do the same thing
# adjective1, adjective2 = input('Enter two adjectives, separated by comma: ').split(',')

# join
# fruits = ', '.join(['apples', 'bananas', 'pears'])
# print(fruits)

# tuple unpacking
# fruit1, fruit2 = ['apples', 'bananas']



person = input('Enter a person: ')
adjective1, adjective2 = input('Enter two adjectives, separated by comma: ').split(',')
noun1, noun2 = input('Enter two nouns, separated by comma: ').split(',')
verb1, verb2 = input('Enter two verbs, separated by comma: ').split(',')


madlib = f"I believe that {person}’s views were the most {adjective1} of all the {adjective2} men in our time. We should strive to do things in his {noun1}: not to use {verb1} in fighting for our cause, but by {verb2} in anything you believe is {noun2}."
print(madlib)
