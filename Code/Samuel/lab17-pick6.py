# PDX Code Guild Fullstack Course
# Lab 17 Pick 6
# Samuel Purdy
# 4/22/2020

import random

# Generates a list of 6 random integers and returns it
def get_ticket():
    ticket = list()
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

# Returns a value equal to the winnings earned if there 
# are multiple matches between the ticket given and the 
# winning numbers
def get_winnings(ticket, winning_ticket):
    matches = 0
    # Compares the values of each index since both lists 
    # are of the same length.
    for i in range(len(winning_ticket)):
        if ticket[i] == winning_ticket[i]:
            matches += 1
    if matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 100
    elif matches == 4:
        return 50000
    elif matches == 5:
        return 1000000
    elif matches == 6:
        return 25000000
    return -2


balance = 0
# Generates a ticket that will win and what is used to 
# compare the purchased ticket against.
winning_ticket = get_ticket()

# Loops 100000 times and incriments the ending balance 
# with whatever winnings are earned.
for i in range(100000):
    balance += get_winnings(get_ticket(), winning_ticket)

print(balance)
