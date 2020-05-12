from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   

   animal = 'armadillo'
   texture = 'scales'
   noun = 'dirt'
   madlib = f'Suzy had a {animal} its {texture} was white as {noun}'
   # passing KWARGS below
   return render_template('index.html', result=madlib)

