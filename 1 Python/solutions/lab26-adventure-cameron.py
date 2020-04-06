'''
Lab 30 - Adventure
• use more succinct commands (l/u/d/r)
• add boundaries to the map, when the player attempts to move beyond the boundary, stop them
• make what's printed on the screen a part of a much larger map
• use different unicode characters
• add player health
• add player score
• add hidden treasure, make the objective to find all the treasure
• add a final boss
• encounter complexity
'''

import random

width = 20  # the width of the board
height = 20  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# player score
enemies_slain = 0
enemies_counter = 0  # separate score to trigger final boss

# player stats
player_goals = 0
player_life = 5
player_treasure = 0

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = 'ο'

# add 4 treasures in random locations
for i in range(4):
    treasure_i = random.randint(0, height - 1)
    treasure_j = random.randint(0, width - 1)
    board[treasure_i][treasure_j] = '\u2004'

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'l':
        if player_j < 1:  # catch if player tries to go beyond left boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_j -= 1  # move left
    elif command == 'r':
        if player_j > 18:   # catch if player tries to go beyond right boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_j += 1  # move right
    elif command == 'u':
        if player_i < 1:   # catch if player tries to go beyond top boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_i -= 1  # move up
    elif command == 'd':
        if player_i > 18:    # catch if player tries to go beyond bottom boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == 'ο':
        print('you\'ve encountered an enemy! (a)ttack or (t)alk')
        action = input('what will you do? ')
        if action == 'a':
            print('you\'ve slain the enemy')
            enemies_slain += 1
            enemies_counter += 1
            board[player_i][player_j] = ' '  # remove the enemy from the board
        if action == 't':
            enemy_outcome = random.randint(0,1)
            if enemy_outcome is 0:
                player_life -= 1
                print('talk is cheap, you took a hit!')
                if player_life < 1:
                    print('...and have been slain!')
                    break
            else:
                    print('You talked it out.')
        elif action != 't' or action != 'a':
            player_life -= 1
            print('you hesitated and took a hit!')
            if player_life < 1:
                print('...and have been slain!')
                break

    # check if the player is on the same space as treasure
    if board[player_i][player_j] == '\u2004':
        board[player_i][player_j] = 'Ξ'
        print('you\'ve found the treasure!')
        player_goals += 1
        if player_goals == 2:
            print('you\'ve beaten then game!')
            break

    # once all enemies have been slayed, reveal final boss
    if enemies_counter == 4:
        boss_i = random.randint(0, height - 1)
        boss_j = random.randint(0, width - 1)
        board[boss_i][boss_j] = 'Ω'
        enemies_counter = 0

    if board[player_i][player_j] == 'Ω':
        print('you\'ve encountered the Final Boss! (a)ttack or (t)alk')
        action = input('what will you do? ')
        if action == 'a':
            print('you\'ve slain the Final Boss!')
            player_goals += 1
            if player_goals == 2:
                print('you\'ve beaten then game!')
                break
        if action == 't':
            print('talk is cheap, you took a hit!')
            player_life -= 1
            if player_life < 1:
                print('...and were slain!')
                break
        elif action != 't' or action != 'a':
            player_life -= 1
            print('you hesitated and took a hit!')
            if player_life < 1:
                print('...and were slain!')
                break

    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('Δ', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
    print('Slays:', enemies_slain)
    print('Life:', player_life)
