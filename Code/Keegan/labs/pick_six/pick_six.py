# Lab 17, Pick Six
# April 21, 2020
import random


def pick_6():
    '''
    Return a list of six random numbers between 1 - 99
    '''
    return [random.randint(1, 99) for i in range(6)]


def find_matching_nums(winner, ticket):
    '''
    Check a ticket against the winning numbers
    and return how many numbers match
    '''

    # counter for number of matches
    counter = 0

    # loop through the length of the ticket
    for i in range(len(ticket)):
        # check each element in ticket against the
        # corresponding index in winner
        if ticket[i] == winner[i]:
            # if the numbers are the same, increment counter
            counter += 1

    return counter


def calculate_payout(number_of_matches):
    '''
    Return monetary winnings based on the number of matches
    '''
    payouts = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 5e4,
        5: 1e6,
        6: 25e6,
    }

    return payouts[number_of_matches]


def cost_of_habit(balance, expenses):
    '''
    Calculate the Return on Investment rate
    '''
    return balance / expenses


def main():
    # Generate a list of 6 random numbers representing the winning ticket
    winner = pick_6()

    # the cost of one ticket
    ticket_cost = 2

    # Start your balance at 0
    balance = 0

    # start earnings and expenses at 0
    earnings = 0
    expenses = 0

    ticket_count = 0

    # Loop 100,000 times, for each loop:
    while ticket_count < 1e5:
        # Generate a list of 6 random numbers representing the ticket
        ticket = pick_6()

        # Subtract 2 from your balance (you bought a ticket)
        balance -= 2
        ticket_count += 1

        # Find how many numbers match
        matches = find_matching_nums(winner, ticket)

        # Add to your balance the winnings from your matches
        payout = calculate_payout(matches)
        # balance += payout
        earnings += payout

        # print(f"{winner  = }")
        # print(f"{ticket  = }")
        # print(f"{matches = }")
        # print(f"{payout  = }")

    expenses = ticket_count * ticket_cost
    balance = earnings - expenses

    # probably don't need a function for this
    roi = cost_of_habit(balance, expenses)

    # print(f'{ticket_count = }')
    # After the loop, print the final balance
    print(f"Your final balance was: ${balance}")
    print(f"Your habit cost you {roi * 100}% of your investment")


main()
