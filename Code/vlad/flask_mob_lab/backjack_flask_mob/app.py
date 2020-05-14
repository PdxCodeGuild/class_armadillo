from flask import Flask, render_template, request
app = Flask(__name__)

blackjack_dict = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
}

@app.route('/', methods=['GET', 'POST']) #path
def index(): #view
    title = 'BLACKJACK MOB'
    if request.method == 'POST':
        form_data = dict(request.form)
        print(form_data)
        # form_data = {'card1': 'A', 'card2': 'A', 'card3': 'A'}
        card1 = int(form_data['card1'])
        card2 = int(form_data['card2'])
        card3 = int(form_data['card3'])
        print(card1, card2, card3)

        # card1 = blackjack_dict[form_data['card1']]
        # card2 = blackjack_dict[form_data['card2']]
        # card3 = blackjack_dict[form_data['card3']]
        
        hand = card1 + card2 + card3
        print(hand)
        
        if hand < 17:
            print('hit')
        elif hand >= 17 and hand < 21:
            print('stay')
        elif hand == 21:
            print('blackjack')
        else:
            print('bust')

    return render_template('index.html', title=title, hand=hand)