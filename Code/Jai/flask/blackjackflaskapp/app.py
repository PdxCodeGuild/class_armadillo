from flask import Flask, render_template, request 


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def index():
    if request.method == 'POST':
        print(request.form)

        cards= {'A':1, 
                'J':10,
                'Q':10,  
                'K':10,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10, }
        card1 = request.form['card1']
        card2 = request.form['card2']
        card3 = request.form['card3']      
        print(card1, card2, card3)
        total = cards[card1] + cards[card2] + cards[card3] 
        print(total)
        
        if total < 17:
            result = 'Hit'
        elif total < 21:
            result = 'stay'
        elif total == 21:
            result = 'BlackJACK'
        else:
            result = 'BUSTED'

    else:
        total = ''
        result = ''
        
    return render_template('index.html', total = total, result = result)