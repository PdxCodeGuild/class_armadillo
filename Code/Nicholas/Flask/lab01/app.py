from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
   
    print(request.form)
    if request.method == 'POST':
        user_input = request.form[float(input("Enter a length in feet to convert to meters: "))]
        meters = feet*0.3048  #feet to meters conversion  
    else: 
        meters = ''     
    return render_template('index.html', result=meters)
    
    
    
