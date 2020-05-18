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
        card_two = request.form['card_choice_two']
        card_three = request.form['card_choice_three']
        # print(request.form)
        blackjack = advice_blackjack.blackjack(card_one,card_two,card_three)
    else:
        blackjack = ''
    return render_template('index.html', deck = deck, blackjack = blackjack)