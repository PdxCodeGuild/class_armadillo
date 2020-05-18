from flask import Flask, render_template, request
import random
import json
app = Flask(__name__)

def load_db():
    with open('db.json', 'r') as file:
        text = file.read()
    return json.loads(text)
    
def save_db(data):
    with open('db.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
        
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
            # or just else:
            elif comp_rps == 'rock':
                result = "User wins!"

        
        elif user_rps == 'scissors':
        # or just else:
            # check scissors against comp_rps
            if comp_rps == 'rock':
                result = "Computer wins!"
            elif comp_rps == 'paper':
            #or just else:
                result = "User wins!"

        data = load_db()
        # data = {'user_score': 0, 'computer_score': 0}
        if result == 'User wins!':
            # increment user_score
            data['user_score'] += 1
            pass
        elif result == 'Computer wins!':
            # increment computer_score
            data['computer_score'] += 1
            pass
        save_db(data)

        return render_template(
            'index.html',
            user_rps=user_rps,
            comp_rps=comp_rps,
            result=result,
            data=data
        )
    # print(f"User chose {user_rps}.")
    # print(f"Computer chose {comp_rps}.")
    # print(result)

    return render_template('index.html')

