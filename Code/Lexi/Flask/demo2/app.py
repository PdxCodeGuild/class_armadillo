from flask import Flask, render_template, request
app = Flask(__name__)

# 1. get basic request-response cycle working https://github.com/PdxCodeGuild/class_armadillo/blob/master/3%20Flask/docs/02%20-%20Flask.md#setup
# 2. render a template - create a templates folder with an index.html
# 3. render a value in the template by passing kwargs to render_template
# 4. put a form in the template, make sure it looks good and captures the data you need
# 5. submit the form, make sure you can see the form data print(request.form)
# 6. do something with the form data, show the output in the template

# this view is both rendering a template (get) and receiving a form submission (post)
# methods - http methods this view will accept
@app.route('/', methods=['GET', 'POST']) # path
def index(): # view
    print(f'in the index view - the request method is {request.method}')

    if request.method == 'POST': # the method of the request is POST meaning the user submitted a form
        form_data = dict(request.form) # convert the incoming form data into a dictionary
        print(form_data)
        # you can use just request.form['mytext']
        mytext = form_data['mytext'] # this will crash if the user sends an HTTP GET (because the request doesn't contain form data)
        print(mytext)

        myddl = form_data['myddl']
        print(myddl)

        # checkboxes work a little strangely
        # if the checkbox is checked, it will come through in the form data with the value 'on'
        # if the checkbox is not checked, it won't come through in the form data at all
        # and the below code will crash
        # mycheckbox = form_data['mycheckbox']
        mycheckbox = 'mycheckbox' in form_data # True if checked, False if not checked
        print(mycheckbox)

        fruit = form_data['fruit']
        print(fruit)

        # here is usually where you do some operation on the form data that was submitted
        # message = f'{mytext=} {myddl=} {mycheckbox=} {fruit=}'
        message = f'mytext={mytext} myddl={myddl} mycheckbox={mycheckbox} fruit={fruit}'
    else:
        message = 'no form data'

    return render_template('index.html', title='Demo App', message=message, a=1, b=2)

# methods - http methods this view will accept
# @app.route('/receive_form', methods=['GET', 'POST'])
# def receive_form():
#     print(dict(request.form))
#     return 'you are at receive form'
