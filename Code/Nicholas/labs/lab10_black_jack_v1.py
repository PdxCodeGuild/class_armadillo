#this lab provides user black jack advice based on the sum of 3 cards

card_values = {  #dictionary of card values
    "A": 1,
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

card1 = input("What is the value of your first card? ").upper()  #takes user card input, converts input to uppercase
card2 = input("What is the value of your second card? ").upper()
card3 = input("What is the value of your third card? ").upper()

sum = (card_values[card1] + card_values[card2] + card_values[card3])  #converts input value to numerical value from dict, sums cards up
print(sum)
#conditions: 
if sum < 17:
    print("hit")  
elif sum < 21:
    print("stay")    
elif sum == 21:
    print("Black Jack!") 
else: 
    print("Already Busted!")       

