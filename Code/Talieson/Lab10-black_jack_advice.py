# Take 3 playing cards from the user

# assign a point value to each card; assume aces are worth 1

# * Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"

# print out current total and the advice


def validate_units(input_units):
    unit_lists = [
        ["A", "a", "Ace", "ACE", "ace"],
        ["K", "k", "King", "KING", "king"],
        ["Q", "q", "Queen", "QUEEN", "queen"],
        ["J", "j", "Jack", "JACK", "jack"],
        ["10", "Ten", "TEN", "ten"],
        ["9", "Nine", "NINE", "nine"],
        ["8", "Eight", "EIGHT", "eight"],
        ["7", "Seven", "SEVEN", "seven"],
        ["6", "Six", "SIX", "six"],
        ["5", "Five", "FIVE", "five"],
        ["4", "Four", "FOUR", "four"],
        ["3", "Three", "THREE", "three"],
        ["2", "Two", "TWO", "two"],
    ]
    for unit_list in unit_lists:
        if input_units in unit_list:
            return unit_list[0]
    print("I'm sorry that's not a valid response. ")
    return None


card_values = {
    "A": [1], "K": [10], "Q": [10], "J": [10], "10": [10], "9": [9],
    "8": [8], "7": [7], "6": [6], "5": [5], "4": [4], "3": [3], "2": [2],
}

run = True

while run:
    player_first_card = input("What is your first card?")
    player_first_card = validate_units(player_first_card)
    player_first_card = card_values[player_first_card][0]
    player_second_card = input("What is your second card?")
    player_second_card = validate_units(player_second_card)
    player_second_card = card_values[player_second_card][0]
    player_third_card = input("what is your third card?")
    player_third_card = validate_units(player_third_card)
    player_third_card = card_values[player_third_card][0]

    card_values_sum = player_first_card + player_second_card + player_third_card

    advice = ""

    if card_values_sum < 17:
        advice = "Hit!"
    elif card_values_sum >= 17 and card_values_sum < 21:
        advice = "Stay, play it cool."
    elif card_values_sum == 21:
        advice = "Black! You're amazing!"
    elif card_values_sum > 21:
        advice = "It's too late for me, you've already Busted.."

    print(f"You have {card_values_sum}, I suggest you {advice}")
