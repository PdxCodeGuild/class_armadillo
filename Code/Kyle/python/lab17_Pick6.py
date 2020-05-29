import random

## create a function to generate X numbers
def generate_ticket():
    ticket = []
    for i in range(num1):
        ticket.append(random.randint(1, 99))
    return ticket

## returns a winnings value
def compare_tickets(ticket, winning_ticket):
    matches = 0
    # loop i | range | length of the whole winning ticket
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




print("Welcome to Lab 17, Pick 6. ")
print("Let's play a few lottery numbers.\n")

# ask the user how many numbers they want in their lottery tickets
num1 = input("How many numbers do you want in each lottery ticket? ")

# check to make sure the input is valid
while not num1.isnumeric():
    print("I'm sorry, I don't understand that response. Please enter a valid non-negative number. ")
    num1 = input("How many numbers do you want in each lottery ticket? ")

#check to make sure the number is between 1 and 16.
while not int(num1) >= 1 and int(num1) <= 16:
    print("Your request is outside the parameters of the game.")
    print("Please pick a number between 1 and 16. ")
    num1 = input("How many numbers do you want in each lottery ticket? ")

num1 = int(num1)

# ask the user how many times they want to play 
num2 = input("How many times do you want to play this game? ")

# check to make sure the input is valid
while not num2.isnumeric():
    print("I'm sorry, I don't understand that response. Please enter a valid non-negative number. ")
    num = input("How many times do you want to play this game? ")

num2 = int(num2)

# generate winning ticket 
winning_ticket = generate_ticket()
result = 0

# run the game num2 times to determine winnings/loses
for i in range(num2):
    result += compare_tickets(generate_ticket(), winning_ticket)
    
# turn the result into a float
result = float(result)

#convert the result into currency
#thank you stack overflow
result = '${:,.2f}'.format(result)

print(f"Your winnings are: {result} over {num2} tickets. Was this a wise investment?" ) 