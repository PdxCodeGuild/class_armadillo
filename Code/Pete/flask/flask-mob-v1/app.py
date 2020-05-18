from flask import Flask, render_template, request
import random

app = Flask(__name__)

moves = [
    'rock',
    'paper',
    'scissors',
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_dict = dict(request.form)
        print(form_dict) #{'rps': 'scissors'}
        user_rps = form_dict['rps']
        print(user_rps)
        comp_rps = random.choice(moves)
        print(comp_rps)

        if user_rps == comp_rps:
            print("It's a tie!")
            result = "It's a tie"

        elif user_rps == 'rock':
            # check rock against comp_rps
            if comp_rps == 'scissors':
                result = "User wins!"
            elif comp_rps == 'paper':
            # or just else:
                result = "Computer wins!"
                
        elif user_rps == 'paper':
            # check paper against comp_rps
            if comp_rps == 'scissors':
                result = "Computer wins!"
            elif comp_rps == 'rock':
            # or just else:
                result = "User wins!"

        
        elif user_rps == 'scissors':
        # or just else:
            # check scissors against comp_rps
            if comp_rps == 'rock':
                result = "Computer wins!"
            elif comp_rps == 'paper':
            #or just else:
                result = "User wins!"

    print(f"User chose {user_rps}.")
    print(f"Computer chose {comp_rps}.")
    print(result)

    return render_template('index.html', user_rps=user_rps, comp_rps=comp_rps, result=result)

