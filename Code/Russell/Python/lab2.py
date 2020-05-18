print('Welcome to MadLib!')

second_lib = 'Y'

while second_lib == 'Y':

    adjective1 = input('Enter an adjective:')
    adjective2 = input('Enter another adjective:')
    adjective3 = input('Enter a third adjective:')

    adverb = input('Adverb:')

    person_name = input('Name a person you know:')

    noun1 = input('Noun:')
    noun2 = input('Enter a second noun:')
    noun3 = input('Enter a third noun:')

    number = input('Enter a number:')
    number2 = input('Enter a second number:')

    plural_noun = input('Plural noun:')
    plural_noun2 = input('Another plural noun:')

    verb = input('Verb:')
    verb2 = input('Another verb:')

    print('"To Whom It May Concern..."')

    print(f"I have known {person_name} for {number} years and {adverb} recommend him/her for the position of assistant {noun1} in your {adjective1} company.") 
    print(f"I can't {verb} enough about this person's {adjective2} character and ability to get along with his/her fellow {plural_noun}.") 
    print(f"As for educational background, {person_name} is a college {noun2}, is capable of speaking several foreign {plural_noun2}, and has an IQ of {number2}.") 
    print(f"You will find {person_name} to be a {adjective3} worker who is not only as smart as a {noun3}, but who doesn't know the meaning of the word {verb2}.")
    print("Unfortunately, this is one of many words this person doesn't know the meaning of.")


    second_lib = input('Would you like to make a second madlib? Y/N:')

    if second_lib == 'N':
        print('Thanks for playing!')