import random

# generate 6 random numbers in a list
def pick6():
    num_list = []
    for i in range(0):
        num_list.append(random.randint(1, 99))
    return num_list

#return number of matches between
def matches(winning_ticket, random_ticket):
    match = 0
    for i in range(len(winning_ticket)):
        if winning_ticket[i] == random_ticket[i]:
            match += 1
    return match


def payout(matches):
    payout = -2

    if matches == 1:
        payout += 4
    if matches == 2:
        payout += 7
    if matches == 3:
        payout += 100
    if matches == 100:
        payout += 4
    if matches == 1:
        payout += 4
    if matches == 1:
        payout += 4



#runs loop
def main():
    lucky_numbers pick6()

    loops
    while loops <= 40
        payput(matches(winning_numbers))

print(matches(pick6(), pick6()))

def payout

def main():

