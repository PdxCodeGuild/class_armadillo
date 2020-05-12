from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    message = ''
    scrambled_word = ""
    if request.method == 'POST':
        rotation = request.form['rotation']
        transform = request.form['transform']
        if not check_if_numeric(rotation):
            message = "Please enter in a whole number either positive, negative, or zero."
        else:
            alphabet_upper = string.ascii_uppercase
            alphabet_lower = string.ascii_lowercase
            digits = string.digits
            punctuation = string.punctuation

            rot_alphabet_upper = str()
            rot_alphabet_lower = str()
            rot_digits = str()
            rot_punctuation = str()

            rotation = int(rotation)
            if rotation > 0:
                rot_alphabet_upper = alphabet_upper[rotation:] + alphabet_upper[:rotation-len(alphabet_upper)]
                rot_alphabet_lower = alphabet_lower[rotation:] + alphabet_lower[:rotation-len(alphabet_lower)]
                rot_digits = digits[rotation:] + digits[:rotation-len(digits)]
                rot_punctuation = punctuation[rotation:] + punctuation[:rotation-len(punctuation)]
            elif rotation < 0:
                rot_alphabet_upper = alphabet_upper[rotation:] + alphabet_upper[:rotation+len(alphabet_upper)]
                rot_alphabet_lower = alphabet_lower[rotation:] + alphabet_lower[:rotation+len(alphabet_lower)]
                rot_digits = digits[rotation:] + digits[:rotation+len(digits)]
                rot_punctuation = punctuation[rotation:] + punctuation[:rotation+len(punctuation)]
            else:
                rot_alphabet_upper = alphabet_upper
                rot_alphabet_lower = alphabet_lower
                rot_digits = digits
                rot_punctuation = punctuation

            for i in range(len(transform)):
                if alphabet_upper.find(transform[i]) > -1:
                    scrambled_word += rot_alphabet_upper[alphabet_upper.find(transform[i])]
                elif alphabet_lower.find(transform[i]) > -1:
                    scrambled_word += rot_alphabet_lower[alphabet_lower.find(transform[i])]
                elif digits.find(transform[i]) > -1:
                    scrambled_word += rot_digits[digits.find(transform[i])]
                elif punctuation.find(transform[i]) > -1:
                    scrambled_word += rot_punctuation[punctuation.find(transform[i])]
                else:
                    scrambled_word += transform[i]
    else:
        scrambled_word = str()
    return render_template("rot13.html", result=scrambled_word, message=message)