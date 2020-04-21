import random
import time


# Create a list of 6 random integers.
def pick6():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 100))
    # Return that list.
    return nums


def num_matches(winning, ticket):
    matches = 0
    # Iterate through the indexes.
    for i in range(6):
        # Check if the values at those indexes match.
        if ticket[i] == winners[i]:
            # If they do, iterate matches.
            matches += 1
    # Return the number of matches.
    return matches


# Takes number of matches and returns winnings.
winnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
}

# Global variables
balance = 0
expenses = 0
play_count = 0

# Set the winning numbers
winners = pick6()
print(f'''
The winning numbers are {winners}!
I have a feeling you're about to be very, very, rich!
''')
time.sleep(2)

# Run the check 10000 times
while play_count <= 10000:
    # User buys the ticket
    expenses -= 2
    # Create a ticket, show it to the user, iterate the play_count
    ticket = pick6()
    print(f"your ticket is {ticket}. Good luck!")
    time.sleep(.2)
    play_count += 1
    # Check number of matches
    num_of_matches = num_matches(winners, ticket)
    # display message based on number of matches
    if num_of_matches == 0:
        print("Aww shucks, not this time!")
    elif num_of_matches == 1:
        print('''
    ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
    You got a match!!! You've earned enough for TWO MORE TICKETS!!!
    ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
        ''')
        time.sleep(1)
    elif num_of_matches > 1:
        print(f'''
    ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    Woooahh! You had {num_of_matches} matches! Lucky you!!
    ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    ''')
        time.sleep(1)

    # Get the winnings from dictionary, update balance
    balance += winnings[num_of_matches]

# find the return on investment for the user.
roi = (balance - expenses)/expenses

print(f"You've spent ${expenses}. You can't take it with you, ammrite?")
print(f"You've won: ${balance}!! Wow you're so lucky!")
print(f"Your ROI is: {roi}! Not too shabby.")
