# Lab02 Todo List: 

# For anyone working on Lab 2, remember to check out these demos. You can run them and put in print statements to understand how they work:
# https://github.com/PdxCodeGuild/class_armadillo/tree/master/Code/Matthew/flask/increment
# https://github.com/PdxCodeGuild/class_armadillo/tree/master/Code/Matthew/flask/increment%20-%20multiple%20views
from flask import Flask, render_template, request, redirect
import json

app = Flask('increment_app')


# opens db.json, reads the text, turns the json into a python dictionary
def load_database():
    with open('db.json', 'r') as file: # open the file
        text = file.read() # read the text
    return json.loads(text) # turn the json string into a python dictionary

# opens db.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)

#=======
@app.route('/') # the view function it default to a GET Method
def index(): 
    #data = load_database()
    #return render_template('index.html', value=data['value'], fav_nums=data['fav_nums'])
    todo = load_database()
    # value = data['value']
    todo = todo["todos"]# setting the todo equal to the todos
    #print(todo)
    return render_template("index.html", todo=todo)
   
#============ save to the database +++++++

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # load the database
    todo = load_database()
    
    # get the data out of the form
    # print(request.form) # ImmutableMultiDict([('')])
    user_input = request.form['user_input']
    priority = request.form['priority']
    # print(todo) 

   # todo.append({"text":user_input,"priority":"low"})# 
    todo["todos"].append({"text":user_input,"priority":priority})

# todo is the variable with a dictionary with the key todos follow by a list of dictionary with two keys value pairs 
#todo = {'todos': [{'text': 'walk the dog'}]}
#  fruits =  {
#         1: "banana"
#         2:"mango"
#         3: "orange"
#     }
# fruits[1] # 
    # # save the data to the database
    save_database(todo)

    # redirect the user back to the home page
    # return 'you are at the submit form view'
    return redirect('/')

@app.route('/strikethrough', methods=['POST'])
def strikethrough():
    # return "Hello"
    # print(dict(request.form))
    strike = dict(request.form) # save it to a variable 
    print(list(strike)) # to print the keys in the dictionary in a list 
    strike = list(strike) # ['walk the dog', 'Eat ', 'walk'] list of the thing I checkout on the todo list

# load to the database
    todo = load_database() # I can call this data_load_db = load_database()
    # print(todo)
    # writing a for loop 
    for item in todo['todos']: # todo is the entire dictionary
        # print(item['text']) # printing the text key of this dictionary todos
        if item['text'] in strike: # we are checking to see if the items on the list have been checked
        #    print(item['text'])
            item.update({"completed":True})# this is to add the completed: true to all the other keys value pairs in the other dictionaries inside the json
            print(item)
    print(todo)
        # save to the database 
    save_database(todo)
    return redirect('/')


# item.update({"completed":True})# this is to add the completed: true to all the other keys value pairs in the other dictionaries inside the json

# updating the dictionary without using the update method as shown above: 
#     >>dict = {'a':1, 'b':2, 'c': 3}
# >>> dict
# {'a': 1, 'b': 2, 'c': 3}
# >>> dict['d'] = 4
# >>> dict
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# json = {'todos':[{'a': 1, 'b': 2}, {'a': 3, 'b':4}]}
#      for item in json['todos']:
# ...     print(item)
# ...
# {'a': 1, 'b': 2}
# {'a': 3, 'b': 4}

# change the HTML  







#=========== MY CODE =========== 

# @app.route('/', methods=['GET'])
# # opens db.json, reads the text, turns the json into a python dictionary
# def load_database():
#     todo = {}
#     with open('db.json', 'r') as file: # open the filetext = file.read() # read the text
        
#     todo = json.loads(text) # turn the json string into a python dictionary
#     todo = todo["todos"]# setting the todo equal to the todos
#     print(todo)
#     return render_template("index.html", todo=todo)


# import json

# def load_database():
#     with open('db.json', 'r') as file:
#         data = json.loads(file.read())
#     return data

# def save_database(data):
#     with open('db.json', 'w') as file:
#         file.write(json.dumps(data, indent=4, sort_keys=True))

# data = load_database()
# print(data)
# print(data['value'])
# data['value'] += 1

# print(data)

# save_database(data)


#================================ SAMPLE FROM INSTRUCTOR ===========

# from flask import Flask, render_template, request, redirect
# import json

# app = Flask('increment_app')


# # opens db.json, reads the text, turns the json into a python dictionary
# def load_database():
#     with open('db.json', 'r') as file: # open the file
#         text = file.read() # read the text
#     return json.loads(text) # turn the json string into a python dictionary

# # opens db.json, turns the python dictionary into json, and saves it to the file
# def save_database(data):
#     with open('db.json', 'w') as file: # open the file
#         text = json.dumps(data, indent=4) # turn the python dictionary into a json string
#         file.write(text)



# # request/response cycle 1
# # 1. user goes to http://localhost:5000/ and sends a GET request, which goes to the 'index' view
# # 2. the server responds with the rendered template containing the form

# # request/response cycle 2
# # 3. the user submits the form, which goes to the 'submit_form'
# # 4. the server responds with an instruction to redirect to the 'index' view

# # request/response cycle 3 - the same as request/response cycle 1


# # by default views can only receive GET requests
# # @app.route('/', methods=['GET'])
# @app.route('/')
# def index():
#     #data = load_database()
#     #return render_template('index.html', value=data['value'], fav_nums=data['fav_nums'])
#     data = load_database()
#     value = data['value']
#     fav_nums = data['fav_nums']
#     return render_template('index.html', value=value, fav_nums=fav_nums)


# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     # load the database
#     data = load_database()
    
#     # get the data out of the form
#     print(request.form) # ImmutableMultiDict([('inc_or_dec', 'increment')])
#     inc_or_dec = request.form['inc_or_dec']
#     print(inc_or_dec) # increment

#     # modify the data from the database
#     if inc_or_dec == 'increment':
#         data['value'] += 1
#     else:
#         data['value'] -= 1

#     # save the data to the database
#     save_database(data)

#     # redirect the user back to the home page
#     # return 'you are at the submit form view'
#     return redirect('/')


# @app.route('/save_number', methods=['POST'])
# def save_number():
#     mynumber = request.form['mynumber']
#     mynumber = int(mynumber) # the value form the form is a string by default
#     data = load_database()
#     data['fav_nums'].append(mynumber)
#     data['fav_nums'].sort()
#     save_database(data)

#     return redirect('/')