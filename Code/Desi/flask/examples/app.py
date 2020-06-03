# from flask import Flask, request, render_template
# app = Flask(__name__)
# import string
# import random

# @app.route ('/', methods=["GET", "POST"])
# def hello_word():
#     return "Hello World!"




# from flask import Flask
# app = Flask(__name__)

# @app.route ('/')
# def index():
#     html = '<html><head></head><body>'
#     html = '<ul>'
#     for i in range(100):
#         html += f'<li>{i}</li>'
#     html += '</ul>'
#     html += '</body></html>'
#     print(html)

#     return html


@app.route ('/about')
def about():
    return "welcome to the about page"

