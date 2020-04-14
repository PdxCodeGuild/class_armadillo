#Version 2 install plugin 'Bracket Pair Colorizer'
# alt + tab is how you switch screens on WINDOWS
#to remove 2nd column values, click Ctrl + D, highlight colons,
# then hit Shift + Ctrl + End to select all values after the colon and delete
card_values = {
    "A": [1, 11],
    "2": [2, 2],
    "3" : [3, 3],
    "4" : [4, 4],
    "5" : [5, 5],
    "6" : [6, 6],
    "7" : [7, 7],
    "8" : [8, 8],
    "9" : [9, 9],
    "10" : [10, 10],
    "J" : [10, 10],  
    "Q" : [10, 10],
    "K" : [10, 10],
    }


card_1 = (input("What's  your first card?: "))

card_2 = input("What's your second card?: ")

card_3 = input("What's your third card?: ")


sum_1 = (card_values[card_1][0] + card_values[card_2][0] + card_values[card_3][0])
sum_2 = (card_values[card_1][1] + card_values[card_2][1] + card_values[card_3][1])
# using square brackets on an int will make it crash
# object is not subscriptable ERROR
# handle with 'if' statement || use existing dict
# adv of latter option: line 26 will work
print(sum_1)

if sum_1 < 17:
    print(f'{sum_1} "Hit" ')
elif sum_1 >= 17 and sum_1 < 21: 
    print(f'{sum_1} "Stay" ')
elif sum_1 == 21:
    print(f'{sum_1} "You won!" ')
else:
    print(f'{sum_1} "Already Busted" ')

#to rename vars en masse, hit CTRL + D WINDOWS
# CMD + D on MAC

if sum_2 < 17:
    print(f'{sum_2} "Hit" ')
elif sum_2 >= 17 and sum_2 < 21: 
    print(f'{sum_2} "Stay" ')
elif sum_2 == 21:
    print(f'{sum_2} "You won!" ')
else:
    print(f'{sum_2} "Already Busted" ')
