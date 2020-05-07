"""
Lab 16: Contact List

Let's build a program to manage a list of contacts, using a JSON file. Create a 
text file in the same folder as your lab, paste the following content, and save 
it as "contacts.json".

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

Once you've processed the file, your list of contacts will look something like 
this...

contacts = [
    {'name':'joe', 'age': 34, 'email': 'joe@gmail.com', 'favorite color':'blue'},
    {'name':'jane', 'age': 43 ...}
]

Then implement the following operations in a REPL:

-Create a contact: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
-Retrieve a contact: ask the user for the contact's name, find the user with the given name, and display their information
-Update a contact: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
-Delete a contact: ask the user for the contact's name, remove the contact with the given name from the contact list.
-List a contact: list all the contacts and their information
-Exit: save the contacts to a file and exit the program

Example run:

Welcome to the Contact Manager 5000(tm)!
What operation would you like to perform? create
What is the contact's name? Bob
What is the contact's age? 56
What is the contact's email? bob@email.com
What is the contact's favorite color? blue
Contact Bob has been added!
What operation would you like to perform?

"""

import json

def save_contacts(path, contacts):
    contacts = {'contacts': contacts} # put the list of contacts in to a dictionary
    with open(path, 'w') as file: # open the file
        text = json.dumps(contacts, indent=4, sort_keys=True) # convert our list of dictionaries into json
        file.write(text) # write the json to the file

while True:
    crudle = str("What would you like to do with your contact list? Your options are create, retrieve, update, delete, list, or exit. ").lower
    
    if crudle == "create":
        print(f"You entered {crudle}") #create a new dictionary and append contact (a list of dictionaries))
        name = input("What is the contacts first name? ")
        age =  input("Enter the contacts age? ")
        email = input("Enter the contacts email. ")
        favorite_color = input("What is the contacts favorite color? ")
        cre_contact = {
        "name": name,
        "age": age,
        "email": email,
        "favorite color": color
    }
    contacts.append(cre_contact)
    # elif crudle == "retrieve":
    #     print(f"You entered {crudle}") 
    #     ret_contact = 

    # elif crudle == "update":
    #     print(f"You entered {crudle}")
    #     upd_contact =

    # elif crudle == "delete":
    #     print(f"You entered {crudle}")
    #     del_contact = 

    # elif crudle == "list":
    #     print(f"You entered {crudle}")
    #     list_contacts = 
    # elif crudle == "exit":
    #     print("Goodbye. ")

    # else:
    #     print(f"You entered: {crudle} Please, try again or type exit") 

# saving our contacts to the file
save_contacts(path, contacts)