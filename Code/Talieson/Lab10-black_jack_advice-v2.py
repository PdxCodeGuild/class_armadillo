# in process solution to black_jack_advice-v2.. still some issues.

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
    "A": [1, 11], "K": [10], "Q": [10], "J": [10], "10": [10], "9": [9],
    "8": [8], "7": [7], "6": [6], "5": [5], "4": [4], "3": [3], "2": [2],
}

run = True

while run:
    cards = []
    players_hand = []
    max_hand_size = 3

    while len(cards) < max_hand_size:
        players_card = input("What is your next card? ")
        cards.append(players_card)

    for card in cards:
        card = validate_units(card)
        print(card)
        card = card_values[card][0]
        print(card)
        players_hand.append(card)
        print(players_hand)

    card_value = sum(players_hand)

    for card in players_hand:
        if card == 1 and card_value < 17:
            card = card_values["A"][1]
    
    final_card_value = sum(players_hand)

    advice = ""

    if final_card_value < 17:
        advice = "Hit!"
    elif final_card_value >= 17 and final_card_value < 21:
        advice = "Stay, play it cool."
    elif final_card_value == 21:
        advice = "Black! You're amazing!"
    elif final_card_value > 21:
        advice = "It's too late for me, you've already Busted.."

    print(f"You have {final_card_value}, I suggest you {advice}")
