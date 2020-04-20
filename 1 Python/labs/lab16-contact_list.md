
# Lab 16: Contact List


Let's build a program to manage a list of contacts, using a JSON file. Create a text file in the same folder as your lab, paste the following content, and save it as "contacts.json".

```json
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
```

```python
import json

def load_contacts():
    with open('contacts.json', 'r') as file:
        text = file.read()
    contacts = json.loads(text)
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        text = json.dumps(contacts)
        file.write(text)
```

Once you've processed the file, your list of contacts will look something like this...
```python
contacts = [
    {'name':'joe', 'age': 34, 'email': 'joe@gmail.com', 'favorite color':'blue'},
    {'name':'jane', 'age': 43 ...}
]
```

Then implement the following operations in a REPL:

- Create a contact: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
- Retrieve a contact: ask the user for the contact's name, find the user with the given name, and display their information
- Update a contact: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
- Delete a contact: ask the user for the contact's name, remove the contact with the given name from the contact list.
- List a contact: list all the contacts and their information
- Exit: save the contacts to a file and exit the program

Example run:
```
Welcome to the Contact Manager 5000(tm)!
What operation would you like to perform? create
What is the contact's name? Bob
What is the contact's age? 56
What is the contact's email? bob@email.com
What is the contact's favorite color? blue
Contact Bob has been added!
What operation would you like to perform?
```