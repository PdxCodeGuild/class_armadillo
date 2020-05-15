# Lab02 Todo List: 

from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
# opens db.json, reads the text, turns the json into a python dictionary
def load_database():
    todo = {}
    with open('db.json', 'r') as file: # open the file
        text = file.read() # read the text
    todo = json.loads(text) # turn the json string into a python dictionary
    todo = todo["todos"]# setting the todo equal to the todos
    print(todo)
    return render_template("index.html", todo=todo)



# @app.route('/', methods=['POST'])
# # saving and loading the database
# def save_database(todo):
#     with open('db.json', 'w') as file:
#         file.write(json.dumps(todo))



# demonstrating how to go between json and a python dictionary
# data = '{"name": "bob"}'
# todo = json.loads(todo) # json string -> python dictionary
# print(todo[0]['text']) # bob
# todo = json.puts(todo) # python dictionary -> json string
# print(todo)


# def save_contacts(path, contacts):
#     contacts = {'contacts': contacts} # put the list of contacts in to a dictionary
#     with open(path, 'w') as file: # open the file
#         text = json.dumps(contacts, indent=4, sort_keys=True) # convert our list of dictionaries into json
#         file.write(text) # write the json to the file

# def load_database():
#     with open('database.json', 'r') as file:
#         data = json.loads(file.read())
#     return data

# opens db.json, turns the python dictionary into json, and saves it to the file
# def save_database(data):
#     with open('db.json', 'w') as file: # open the file
#         text = json.dumps(data, indent=4) # turn the python dictionary into a json string
#         file.write(text)


# # if we used classes
# # db = Database()
# # db.load()
# # db.save()

# @app.route('/', methods=['GET', 'POST'])
# def index():

#     # # json.loads turns a string of json into a dictionary
#     # data = json.loads('{"name":"joe","age":456}')
#     # print(data)
#     # print(data['name']) # joe
#     # data['name'] = 'jane'
#     # # json.dumps turns a dictionary into a string of json
#     # json_string = json.dumps(data)
#     # print(json_string)


#     # data = load_database()
#     # print(data)
#     # data['value'] += 1
#     # save_database(data)

#     data = load_database()
#     if request.method == 'POST':
#         print(request.form) # ImmutableMultiDict([('inc_or_dec', 'increment')])
#         inc_or_dec = request.form['inc_or_dec']
#         print(inc_or_dec) # increment
#         if inc_or_dec == 'increment':
#             data['value'] += 1
#         else:
#             data['value'] -= 1
#         save_database(data)
    
#     return render_template('index.html', value=data['value'], fruits=data['fruits'])