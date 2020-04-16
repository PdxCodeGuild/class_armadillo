# Basic input validation
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


# Library of card values to turn strings into blackjack value
card_values = {
    "A": [1], "K": [10], "Q": [10], "J": [10], "10": [10], "9": [9],
    "8": [8], "7": [7], "6": [6], "5": [5], "4": [4], "3": [3], "2": [2],
}


run = True

# Set card equal to user input, ensure it's valid, then return an int
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

# Take the cards totals
    card_value = player_first_card + player_second_card + player_third_card

# Fill the advice string with the appropriate move
    advice = ""

    if card_value < 17:
        advice = "Hit!"
    elif card_value < 21:
        advice = "Stay, play it cool."
    elif card_value == 21:
        advice = "Blackjack! You're amazing!"
    elif card_value > 21:
        advice = "It's too late for me, you've already busted.."

# Return the advice
    print(f"You have {card_value}, {advice}")
