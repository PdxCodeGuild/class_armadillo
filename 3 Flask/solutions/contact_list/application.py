from flask import Flask, render_template, request
app = Flask(__name__)

import csv

def read_database():
    with open('database.csv') as file:
        contacts = csv.DictReader(file)
        contacts = list(contacts)
    headers = list(contacts[0].keys())
    return headers, contacts


def write_database(headers, contacts):
    with open('database.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(contacts)


@app.route('/', methods=['GET', 'POST'])
def index():
    headers, contacts = read_database()
    if request.method == 'POST':
        contact_name = request.form['contact_name']
        contact_age = request.form['contact_age']
        contact_email = request.form['contact_email']
        contact_fav_color = request.form['contact_fav_color']
        contact = {'name': contact_name,
                    'age': contact_age,
                    'email': contact_email,
                    'favorite color': contact_fav_color}
        contacts.append(contact)
        write_database(headers, contacts)
    return render_template('index.html', headers=headers, contacts=contacts)

