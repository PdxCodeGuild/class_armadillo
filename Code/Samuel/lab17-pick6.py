import random

def get_ticket():
    ticket = list()
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def get_winnings(ticket, winning_ticket):
    matches = 0
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
winning_ticket = get_ticket()

for i in range(100000):
    balance += get_winnings(get_ticket(), winning_ticket)

print(balance)
