from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


# import json
# from flask import Flask, request
# from flask import render_template
# from flask import redirect

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello World!
# # # demonstrating how to go between json and a python dictionary
# # data = '{"name": "bob"}'
# # data = json.loads(data) # json string -> python dictionary
# # print(data['name']) # bob
# # data = json.puts(data) # python dictionary -> json string
# # print(data)

# # # saving and loading the database
# # def save_database(data):
# #     with open('database.json', 'w') as file:
# #         file.write(json.dumps(data))

# # def load_database():
# #     with open('database.json', 'r') as file:
# #         data = json.loads(file.read())
# #     return data


# def _init_(self, content):
#     self.content = content
#     self.done = False

# def _repr_(self):
#     return '<Content %>' % self.content


#     # Let's say we looked this up somewhere
# data = {
#     "2018-01-01": {"Temperature": "50"},
#     "2018-01-02": {"Temperature": "53"},
#     "2018-01-03": {"Temperature": "52"}
# }

# @app.route('/')
# def tasks_list():
#     tasks = task.query.all()
#     return render_templates('list.html', tasks=tasks)

# @app.route('/task', methods==['POST'])
# def add_task():
#     content = request.form['content']
#     if not content:
#         return 'Error'

#     task = Task(content)
#     db.session.add(task)
#     db.session.commit()
#     return redirect()




# # Define our simple function
# def what_was_the_weather_like(date):
#     return str(data[date])

# what_was_the_weather_like("2018-01-01")

# # This should return:
# # "{'Temperature': '50'}"





from flask import Flask, render_template, request
import json

#defines variable app and assigns it from Flask.
app = Flask(__name__)

# defines the function for chores.
def load_chores():
    # opens the file.
    with open('database.json', 'r') as file:
        # reads the text
        text = file.read()
    # turns the json string into a python dictionary.
    return json.loads(text)

# saving and loading the database.
def save_chores(data):
    # opens the file to be written.
    with open('database.json', 'w') as file:
        # python dictionary -> json string
        text = json.dumps(data, indent=4)
        # writes the file.
        file.write(text)
        # print(data)

# view is set to GET and POST.
@app.route('/', methods=['GET', 'POST'])
# assigns the function.
def index():
    # assigns variable to the function. 
    data = load_chores()
    # renders the template and runs the html file and accesses the value at the specified objects json key.
    return render_template('index.html', honey_do_list=data['honey_do_list'])    

@app.route('/savehoney_do_list/', methods=['POST'])

def savehoney_do_list():
    


    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
    return render_template('index.html')
    


chore = '{"chore": "mow_the_lawn"}'
data = json.loads(database) # json string -> python dictionary
print(data['chore']) # bob

