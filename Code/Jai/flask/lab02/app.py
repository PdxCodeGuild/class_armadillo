import json 
from flask import Flask, render_template, request



app = Flask(__name__) 
data= load_database()
#print(data)


def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

def load_database(data):
    with open('database.json', 'r') as file:
        data = json.loads(file.read())

print(data)





print(save_database)
@app.route('/', methods = ['GET', 'POST'])

def index():
       for in data
           if  







      
      
       #save_database()
      # if 


        output = ""
    print(request.form)



    return render_template("index.html",  ):
