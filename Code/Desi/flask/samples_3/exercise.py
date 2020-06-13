
from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World'

@app.route('/')
def index():
    html = '<html><head></head></body>'
    html += '<ul>'
    for i in range(100):
        html += f'<li>{i}</li>'
    html += '<ul>'
    html += '</body></html>'
    print(html)

    # return 'Welcome to the home page'

    


