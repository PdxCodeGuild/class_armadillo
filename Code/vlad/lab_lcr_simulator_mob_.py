#Lab LCR Simulator Mob:

""" 
Lab: LCR Simulator
LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves. Description from wikipedia:

Each player receives 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on his/her turn, rather than rolling all three. When a player has zero chips, he/she passes the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot. If he/she chooses to play another round, he/she does not roll 3, he/she keeps his pot and plays with that.

When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.
"""

# LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves. Description from wikipedia:

# Each player receives 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.
# If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on his/her turn, rather than rolling all three. When a player has zero chips, he/she passes the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot. If he/she chooses to play another round, he/she does not roll 3, he/she keeps his pot and plays with that.
# When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.
import random


def roll_dice():
    dice = ['L', 'C', 'R', '1', '1', '1']
    return random.choice(dice)

def main():
    player_list = [
        {
            'name': 'Jon',
            'chips': 3,
        },
    ]
    while True:
        user_input = input('Please enter in a name (done): ')
        if user_input != 'done':
            player = {'name': user_input, 'chips': 3}
            player_list.append(player)
            continue
        else:
            break

    print(player_list)
    # print(player_list[0]['chips'])
    # print(player_list[0]['name'])
    center_pot = 0
    game_loop = True
    while game_loop:
        for i in range(len(player_list)):
            print(f"{player_list[i]['name']}'s turn")

            if player_list[i]['chips'] >= 3:
                dices = 3
            else:
                dices = player_list[i]['chips']

            for dice_rolls in range(dices):
                print(f"Total Chips: {player_list[i]['chips']}")
                
                if player_list[i]['chips'] == 0:
                    break

                random_choice = roll_dice()
                print(f"Rolled a: {random_choice}")

                if random_choice == 'L':
                    if i == player_list[0]:
                        player_list[-1]['chips'] += 1
                        continue
                    player_list[i]['chips'] -= 1
                    player_list[i-1]['chips'] += 1
                elif random_choice == 'R':
                    if i == (len(player_list) - 1):
                        player_list[0]['chips'] += 1
                        continue
                    player_list[i]['chips'] -= 1
                    player_list[i+1]['chips'] += 1
                elif random_choice == 'C':
                    player_list[i]['chips'] -= 1
                    center_pot += 1
                elif random_choice == '1':
                    continue
        
            # Three times the number of players = the number of tokens
            total_tokens = 3*len(player_list)
            if (player_list[i]['chips'] + center_pot) == total_tokens:
                print(f"{player_list[i]['name']} you won!")
                print(f"Total Chip POT {player_list[i]['chips']}")
                print(f'{total_tokens}')
                game_loop = False
            else:
                continue
   
main()