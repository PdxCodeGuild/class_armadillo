import random

# to do:
#    - create a REPL to ask for the players names
#    - test to see if a player has won. 
#    - if a player has won, add the chips in the center pot to 
#      their total and congratulate them.
#    - Add more readable output to the user describing 
#      chip totals and how many dice they get to roll each turn




# create a list of dictionaries for the players
players = [
    {
        'name' : 'Keegan',
        'chips': 0,
    },
    {
        'name' : 'Jai',
        'chips': 3,
    },
    {
        'name' : 'Lawrence',
        'chips': 3,
    },
]

# define six die faces
die_faces = ['l', 'c', 'r', '*', '*', '*']

# pot starts at zero chips
center_pot = 0

# use the player counter to set an index
current_player_index = 0

playing = True
# start game loop
while playing:
    # use the index to pull our player dictionary out of the players list
    current_player = players[current_player_index]

    print(f"\n{current_player['name']}, it's your turn.")
   

    # if the current player has no chips, pass to the next player
    if current_player['chips'] == 0:
        print("You don't get to roll this turn 'cause you have no chips.")
        current_player_index += 1
        continue
    else:
        # if the player has chips, then ask them to roll.
        enter = input('Press enter to roll.')
        while enter != '':
            enter = input('Just press enter to roll.')


    # determine number of dice to roll
    if current_player['chips'] < 3:
        # if the player has less than 3 chips
        # they only get that many dice
        number_of_dice = current_player['chips']
   
    else:
        number_of_dice = 3

    # roll dice
    dice_rolls = []
    for i in range(number_of_dice):
        # add random die face to list of rolls
        dice_rolls.append(random.choice(die_faces))


    for roll in dice_rolls:
        if roll == 'l':
            receiving_player_index = current_player_index - 1
            receiving_player_index %= len(players)
            receiving_player = players[receiving_player_index]

            # remove a chip from the current player
            current_player['chips'] -= 1

            # add a chip to the receiving player
            receiving_player['chips'] += 1

        elif roll == 'r':
            receiving_player_index = current_player_index + 1
            receiving_player_index %= len(players)
            receiving_player = players[receiving_player_index]

            # remove a chip from the current player
            current_player['chips'] -= 1

            # add a chip to the receiving player
            receiving_player['chips'] += 1

        elif roll == 'c':
            # remove a chip from the current player
            current_player['chips'] -= 1
            # add a chip to the center
            center_pot += 1

        elif roll == '*':
            # if a dot, do nothing
            continue
    
    # after current turn is over, 
    # pass the turn to the next player
    current_player_index += 1
    # loop the index back around to 0, 1, or 2 (number of players = 3)
    current_player_index = current_player_index % len(players)

    print(dice_rolls)
    print(players)
    print(f"center: {center_pot}")
