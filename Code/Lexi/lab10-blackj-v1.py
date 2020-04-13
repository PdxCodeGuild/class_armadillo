#dictionary
card_values = {
    "A": 1,
    "2": 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,  # "J" is the key, so 10 is the corr. value
    "Q" : 10,
    "K" : 10,
    }
# Q: would this work in a list, too?
# A: well, how would you put a value into this?

card_1 = (input("What's  your first card?"))

card_2 = input("What's your second card?")

card_3 = input("What's your third card?")

# How do we select a random choice of these? import random

# Matt: let's sum the total value

sum = (card_values[card_1] + card_values[card_2] + card_values[card_3])
print(sum)
#21, if user input J, Q, A

#sum = card_1 + card_2 + card_3
# result : JQA (just concatenated these strings)

# Matt: how do we use the key to look up the value?
# product_to_price['apple']  #> 1.0
# dictionary_name [ 'key_name']

# so using the syntax above on line 37, outlined in ex. 


product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['apple']  #this is how you access 1.0

#prints out 10

# if else statements for advice statements

if sum < 17:
    print("Hit")
elif sum >= 17 and sum < 21: 
    print("Stay")
elif sum == 21:
    print("You won!")
else:
    print("Already Busted")




