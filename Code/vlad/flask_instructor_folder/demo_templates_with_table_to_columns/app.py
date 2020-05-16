# Demo Template showing a table on the index.html see how to configure a table on the index.html
# also the this Demo Template show the database inside the app.py so it does not have a json file but it could be data dictionary can
# be added to a json If I want but this is to demostrate how to get the data our of dictionary 
# by drilling into the layers of dictionary object:

from flask import Flask, render_template
app = Flask('demo_templates')

@app.route('/')
def index():
    data = {
        'contacts': [
            {
                'name': 'joe',
                'age': 45
            },
            {
                'name': 'jane',
                'age': 34
            },
            {
                'name': 'john',
                'age': 67
            }
        ]
    }
    # data = {
    #     'contacts': []
    # }
    
    # nums = [1, 2, 3]
    # print(len(nums)) # 3
    # print(nums.__len__()) # 3

    return render_template('index.html', title='Templates Demo', contacts=data['contacts'])