# # Create a contact: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
import json
import os
# contact_name = input("Enter name: ")
# contact_age = input("Enter age: ")
# contact_email = input("Enter email: ")
# contact_gender = input("Enter gender: ")
# /Users/alex/Desktop/class_armadillo/Code/Lexi/lab16-cre_con.py

person = {
    'name': 'jane', 
    'age': 34
    }                   # python dictionary

json_person = json.dumps(person) # convert a dictionary to a string containing json
person = json.loads(json_person) # convert a string containing json to a dictionary
let person = {name: 'jane', age: 34} # javascript object
let json_person = JSON.stringify(person) # convert a javascript object into a string containing json
person = JSON.parse(json_person) # convert a string containing json into a javascript object

{
    "contacts": [{
        "name": "Joe",
        "age": 34,
        "email": "joe@email.com",
        "favorite color": "blue"
    },{
        "name": "Jane",
        "age": 43,
        "email": "jane@email.com",
        "favorite color": "green"
    },{
        "name": "Jill",
        "age": 65,
        "email": "jill@email.com",
        "favorite color": "orange"
    }]
}

# Create a new Python file an import JSON.
# Crate a dictionary in the form of a string to use as JSON.
# Use the JSON module to convert your string into a dictionary.
# Retrieve a contact: ask the user for the contact's name, find the user with the given name, and display their information

# Update a contact: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a contact: ask the user for the contact's name, remove the contact with the given name from the contact list.
# List a contact: list all the contacts and their information
# Exit: save the contacts to a file and exit the program