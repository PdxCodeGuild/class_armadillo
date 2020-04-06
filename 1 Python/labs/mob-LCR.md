
# Lab: LCR Simulator

LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves. Description from [wikipedia](https://en.wikipedia.org/wiki/LCR_(dice_game)):


> Each player receives 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

>If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on his/her turn, rather than rolling all three. When a player has zero chips, he/she passes the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot. If he/she chooses to play another round, he/she does not roll 3, he/she keeps his pot and plays with that.

When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.
