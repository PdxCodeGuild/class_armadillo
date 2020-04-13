# Version 1

card_values = {
    "ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

card_1 = input("What's your first card? ")
card_2 = input("What's your second card? ")
card_3 = input("What's your third card? ")

sum = (card_values[card_1]) + (card_values[card_2]) + (card_values[card_3])

if sum < 17:
    print("Hit")
elif sum >= 17 and sum <21:
    print ("Stay")
elif sum == 21:
    print("You won!")
else:
    print("Already Busted")
