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