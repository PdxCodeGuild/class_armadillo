
import random

def pick6():

    return [random.randint(1, 99) for i in range(6)]

    # numbers = []
    # for i in range(6):
    #     numbers.append(random.randint(1, 99))
    # return numbers

def num_matches(ticket, winners):
    num_winners = 0
    for i in range(6):
        if ticket[i] == winners[i]:
            num_winners += 1
    return num_winners

    # return sum([1 if ticket[i] == winners[i] else 0 for i in range(6)])



for j in range(100000):

    i = 0
    # balance = 0
    winning_ticket = pick6()
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    earnings = 0

    while i < 100:
        i += 1
        ticket = pick6()
        matches = num_matches(ticket, winning_ticket)

        earnings += payout[matches]

    expenses = 2*100
    balance = earnings - expenses

    if balance > 0:
        print(balance)
    #print((earnings - expenses) / expenses)

















