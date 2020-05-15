#Lab 17: Pick6

import random

# generate 6 random numbers in a list
def get_pick6():
    num_list = []
    for i in range(6):
        num_list.append(random.randint(1,99))
    return num_list

# iterate over pick6 numbers and random numbers and check for matches
# purpose of this function is to return number of matche between the tickets
def get_matches(winning_ticket, random_ticket):
    matches = 0
    print(winning_ticket)
    print(random_ticket)
    for i in range(len(winning_ticket)):
        if winning_ticket[i] == random_ticket[i]:
            matches += 1
    print(matches)
    return matches

# purpose of function is to return payout depending on how many matches were made.
def get_payout(matches):
    payout = -2

    if matches == 1:
        payout += 4
    if matches == 2:
        payout += 7
    if matches == 3:
        payout += 100
    if matches == 4:
        payout += 50000
    if matches == 5:
        payout += 1000000
    if matches == 6:
        payout += 25000000

    return payout



# runs loop
def main():
    # locked in winning numbers outside of loop.
    lucky_numbers = get_pick6()
    payout = 0

    loops = 0
    while loops <= 5000:
        # LOOK UP EXAMPLES OF CALL STACK
        # The inner functions need to run before the outer functions can return anything.
        # Think of it as a book. The outer most function is on the bottom of the pile and the books/functions on top need to run before you can get to the bottom.
        payout += get_payout(get_matches(lucky_numbers, get_pick6()))

        loops += 1

    print(f'The payout was {payout}!')
main()
    
# get_matches(winning_ticket, random_ticket)
