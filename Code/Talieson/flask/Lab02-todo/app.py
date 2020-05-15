import json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def load_database():
    with open('db.json', 'r') as file:
        tasks = json.loads(file.read())
    # if request.method == "POST":
    #     with open('db.json', 'r') as file:
    #         data = json.dumps(file.read())
    print(tasks)
    return render_template("index.html", tasks=tasks["todos"])

# data = json.puts(data) # python dictionary -> json string
# print(data)

# # saving and loading the database
# def save_database(data):
#     with open('database.json', 'w') as file:
#         file.write(json.dumps(data))

# def load_database():
#     with open('database.json', 'r') as file:
#         data = json.loads(file.read())
#     return data