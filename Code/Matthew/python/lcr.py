import random
import time


def print_players(players):
    for player in players:
        print(player["name"] + ":" + str(player["chips"]), end=" ")
    print()

def roll_die():
  dice_results = ["Left", "Right", "Center", ".", ".", "."]
  return random.choice(dice_results)

# takes the players (list of dicts) as a parameter
# returns the winning dict if it exists otherwise returns None
def find_winner(players):
    winner = None
    for player in players:
        if player['chips'] > 0:
            if winner is None:
                winner = player
            else:
                winner = None
                break
    return winner

def get_players():
    players = []
    while True:
        # ask the user to enter the player names
        user = input("Please enter player name. ")
        if user in ["done", "quit", "exit"]:
            break
        elif user.isalpha():
            # each player starts with 3 chips
            players.append({"name": user, "chips": 3})
        else:
            print("Not a valid entry.")
    return players


# global variables

center = 0
players = get_players()

i = 0
while True:

    winner = find_winner(players)
    if winner is not None:
        winner['chips'] += center
        center = 0
        print(f"{winner['name']} is the winner! They won {winner['chips']} chips!")
        if input("Play again? (y/n) ").lower().strip() == "y":
            # reset the game
            for player in players:
                player["chips"] = 3
            center = 0
            i = 0
            break
        else:
            print('thanks for playing!')
            exit()
            
    # if the player has less than 3 chips, they roll the same number of dice they have chips
    # roll 3 dice
    num_dice = min(players[i]['chips'], 3)

    print(f'{players[i]["name"]}\'s turn!')
    for die_i in range(num_dice):
        
        result = roll_die()
        print('\t'+result)
        time.sleep(1)
        # if the die is L, move a chip to the player on the left (i-1)
        if result == "Left":
            players[i]["chips"] -= 1
            left_index = i-1
            if left_index < 0:
                left_index = len(players) - 1
            players[left_index]["chips"] += 1
        # if the die is R, move a chip to the player on the right (i+1)
        elif result == "Right":
            players[i]["chips"] -= 1
            right_index = i+1
            if right_index >= len(players):
                right_index = 0
            players[right_index]["chips"] += 1
        # if the die is C, move a chip to the center pot
        elif result == "Center":
            players[i]["chips"] -= 1
            center += 1
    print_players(players)
    print()
    i += 1
    if i == len(players):
        i = 0
