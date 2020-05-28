from flask import Flask, render_template, request # importing Flask
app = Flask('rot13') # create a Flask app, give it a name


# using a single alphabet string
def rot13(text, n=13):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  output = ''
  for char in text: # iterate over the characters in text
    index = alphabet.find(char) # find the index of the character in the alphabet
    index += n
    index %= len(alphabet)
    output += alphabet[index]
  return output


# localhost:5000/
# methods - http methods we allow for this view
@app.route('/', methods=['GET', 'POST']) # defining a route - a place to interact with the web application
def index(): # view - function that receives the request and returns a response
    
    if request.method == 'POST': # the request method will be POST if we submitted a form
        
        # print will show in the terminal on the server
        # it's good for debugging but the user will never see it
        print(dict(request.form)) # {'input_text': 'hello world', 'rotation_amount': '20'}
        input_text = request.form['input_text']
        rotation_amount = int(request.form['rotation_amount'])
        print(input_text) # hello world
        print(rotation_amount) # 20

        # actually do rot 13
        output = rot13(input_text, rotation_amount)

    else: # the request method will be GET if we go the page directly
        output = ''
    return render_template('index.html', title='Rot13', output=output) # respond with a template

# localhost:5000/hello/
@app.route('/hello/') # defining a route - a place to interact with the web application
def hello(): # view - function that receives the request and returns a response
    return 'Hello World!'

# localhost:5000/about/
@app.route('/about/') # defining a route - a place to interact with the web application
def about(): # view - function that receives the request and returns a response
    return 'About Page'