# Black Jack Advice allows you to input 3 cards and outputs advice on how
# to play that hand.


# unit validation, loops through the list of lists grabs the first value
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


# This library sets the value of cards based on the inputs.
card_values = {
    "A": 1, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9,
    "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
}

run = True
# This is the main run loop
while run:
    # establish players hand to add values to.
    players_hand = []

    # takes players cards, and calls the validation function on them.
    while len(players_hand) != 3:
        players_input = input("Enter your card: ")
        players_input1 = validate_units(players_input)

        # if it comes back invalid, asks again.
        while not players_input1:
            print("That is not a valid response.")
            players_input = input("Enter your card: ")
            players_input1 = validate_units(players_input)

        # If valid input, refer to library for card value and add it to hand
        if players_input:
            players_card = card_values[players_input1]
            players_hand.append(players_card)

    # if we have any aces and we're not busting, add 10 to the hand
    for card in players_hand:
        if 1 in players_hand and sum(players_hand) < 11:
            players_hand.append(10)

    final_card_value = sum(players_hand)

    advice = ""

    if final_card_value < 17:
        advice = "Hit!"
    elif final_card_value < 21:
        advice = "Stay, play it cool."
    elif final_card_value == 21:
        advice = "Blackjack! You're amazing!"
    elif final_card_value > 21:
        advice = "It's too late for me, you've already busted.."

    # generates advice.
    print(f"You have {final_card_value}, {advice}")

    # set run to false and ask if they have more checks.
    run = False

    while not run:
        go_again = input("Do you need more advice? (Y/N) ")
        if go_again == "Y":
            run = True
            break
        if go_again == "N":
            exit()
        else:
            print("That is not a valid response.")
