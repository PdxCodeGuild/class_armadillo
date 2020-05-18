from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__) 

#print(data)



def load_database():
    with open('database.json', 'r') as file: # open the file
        text = file.read() # read the text
    return json.loads(text) # turn the json string into a python dictionary


def save_database(data):
    with open('database.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)


@app.route('/', methods = ['GET', 'POST'])

def index():
   data = load_database()
   print(data) 
   return render_template("index.html", title= "todo list", todos= data['todos'])

@app.route('/newtask', methods = ['POST'])
def savetask():
    print(request.form)
    newtask = request.form['new_task']
    priority = request.form['priority']
    data = load_database()
    data['todos'].append({'task':newtask, 'priority': priority })
    
    save_database(data)
    

    return redirect('/')
    
