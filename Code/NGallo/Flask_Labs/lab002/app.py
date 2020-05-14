from flask import Flask, render_template, request
# import python_for_lab.blackjack as blackjack
from python_for_lab import advice_blackjack
# import random

# random.shuffle()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    deck = advice_blackjack.deck
    if request.method == 'POST':
        card_one = request.form['card_choice_one']
        # card_two = request.form['card_choice_two']
        card_two = 'A'
        card_three = request.form['card_choice_three']
        # print(request.form)
        advice_blackjack.blackjack(card1,card2,card3)
    else:
        pass
    return render_template('index.html',deck = deck)