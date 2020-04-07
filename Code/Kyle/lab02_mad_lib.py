# >>> Give me an antonym for 'data': nonmaterial
# >>> Tell me an adjective: Bearded
# >>> Give me a sciency buzzword: half-stack
# >>> A type of animal (plural): parrots
# >>> Some Sciency thing: warp drive
# >>> Another sciency thing: Trilithium crystals
# >>> Sciency adjective: biochemical

# >>> Nonmaterial Scientist Job Description:
# >>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
# >>> Key responsibilities:
# >>> - Extract patterns from non-material
# >>> - Optimize warp drive
# >>> - Transform trilithium crystals into biochemical material.

data_antonyms = ['Conjecture', 'Assumption', 'Problem', 'Proposition', 'Inference', 'Deduction']
adjectives = ['Georgian', 'plaid', 'tiresome', 'callous', 'gruesome', 'hulking', 'verdant']
sciency_buzzword = ['Big Data', 'Machine Learning', 'Internet of Things', 'Quantum Computing', 'Blockchain', 'Singularity']
animals = ['tigers', 'lemurs', 'sabertooth tigers', 'marmots', 'snakes', 'camels']
sciency_things = ['Hyperdrive', 'Fusion Reactor', 'Nanoparticles', 'Cryptocurrency', 'Artificial Intelligence', 'Extra-Solar Runestones']
sciency_adverbs = ['Optimize', 'Synergize', 'Concatenate', 'Transform', 'Alchemate']
sciency_adjectives = ['cybernetic', 'biotic', 'technological', 'cryptological']

import random

initial_query = input("Do you want to play a game?")

affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']

if initial_query.lower() in affirmatives:
  data_antonyms_query = input("Please enter three antonyms of the word 'data', all separated by commas: ").split(',')
  adjectives_query = input("Please enter three adjectives, all separated by commas: ").split(',')
  sciency_adjectives_query = input("Please enter three 'sciency adjectives,' all separated by commas: ").split(',')
  animals_query = input("Please enter three animals, all separated by commas: ").split(',')

  print(f'{random.choice(data_antonyms_query)} Scientist Job Description: ')
  print(f'Seeking a{random.choice(adjectives_query)} engineer, able to work on{random.choice(sciency_adjectives_query)} projects with a team of{random.choice(animals_query)}.')

else:
  print(f'{random.choice(data_antonyms)} Scientist Job Description:')
  print(f'Seeking a {random.choice(adjectives)} engineer, able to work on {random.choice(sciency_adjectives)} projects with a team of {random.choice(animals)}.')

# else:
#   follow_up_game = input('Do you want to play again? ')
#   if follow_up_game.lower() in affirmatives:
#     print(mad_lib_user_input)
#   else:
#     print('Thanks for playing! ')


