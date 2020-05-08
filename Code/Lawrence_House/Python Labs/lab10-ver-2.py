card_values = {
    "ace": [1,11],
    "2": [2,0],
    "3": [3,0],
    "4": [4,0],
    "5": [5,0],
    "6": [6,0],
    "7": [7,0],
    "8": [8,0],
    "9": [9,0],
    "10": [10,0],
    "J": [0,0],
    "Q": [0,0],
    "K": [0,0],
}

card_1 = input("What's your first card? ")
card_2 = input("What's your second card? ")
card_3 = input("What's your third card? ")

sum_1 = (card_values[card_1]) + (card_values[card_2]) + (card_values[card_3])
sum_2 = ()
if sum < 17:
    print("Hit")
elif sum >= 17 and sum <21:
    print ("Stay")
elif sum == 21:
    print("You won!")
else:
    print("Already Busted")