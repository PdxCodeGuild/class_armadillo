import json
import time

# print(json.dumps(contacts, indent=4, sort_keys=True))

contacts = {"contacts": [
        {
            "age": 34,
            "email": "joe@email.com",
            "favorite color": "blue",
            "name": "Joe"
        },
        {
            "age": 43,
            "email": "jane@email.com",
            "favorite color": "green",
            "name": "Jane"
        },
        {
            "age": 65,
            "email": "jill@email.com",
            "favorite color": "orange",
            "name": "Jill"
        }
    ]
}

# print(contacts['contacts'][0]['name'])

def load_contacts(path):
    with open(path, 'r') as file: # open file
        text = file.read() # read the file
    contacts = json.loads(text) # convert json to dictionary
    contacts = contacts['contacts'] # extract the list inside dict
    return contacts

def save_contacts(path, contacts):
    contacts = {'contacts': contacts} # put the list of contacts into a dictionary
    with open(path, 'w') as file: # open the file
        text = json.dumps(contacts, indent=4, sort_keys=True) # convert list of dictionaries into json
        file.write(text) # write the json to the file 

        
             
# loading the contacts from the file
path = 'contacts.json'
contacts = load_contacts(path)

# print(contacts)
# print(type(contacts))

# print(contacts[0]['name'])
# print(contacts['contacts'][0]['name'])
print('\nWelcome to your CONTACT LIST...')

time.sleep(1)

print('Available commands: create, retrieve, update, delete, list, save, exit')

time.sleep(1)

while True:
    command = input('\nState command: ')
    if command in ['stop', 'done', 'exit', 'quit']:
        break
    elif command == 'create':
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        email = input('Enter e-mail: ')
        color = input ('Enter favorite color: ')
        card = { # inserts the above user input into dictionary format
            'name': name,
            'age': age,
            'email': email,
            'favorite color': color,
        }
        contacts.append(card) # adds the above 'card' variable to the 'contacts' JSON file
    elif command == 'retrieve':
        name = input('Enter name: ') # uses name entry to retrieve the appropriate contact
        found_contact = False # boolean for input validation
        for card in contacts:
            if name.lower() in card['name'].lower(): # .lower() makes entry case insensitive
                print(card['name']) # contact name as listed in JSON plus below JSON info formatted
                print('    Age:', card['age'], '    e-mail:', card['email'], '    Favorite color:', card['favorite color'])
                found_contact = True # input validation
        if not found_contact: # if found_contact = False
            print('No contact found.') 
    elif command == 'update':
        name = input('Enter name: ')   
        for card in contacts:
            if name.lower() == card['name'].lower(): # case insensitive, selects contact if name associated with entered name
                name = input('Enter updated name: ') # input for overwriting selected contact
                age = int(input('Enter updated age: '))
                email = input('Enter updated e-mail: ')
                color = input ('Enter updated favorite color: ')
                card['name'] = name #overwrites current contact info with inputs  
                card['age'] = age
                card['email'] = email
                card['favorite color'] = color
                break 
        else: 
            print('No contact found.')
    elif command == 'delete':
        name = input('Enter name: ')
        for card in contacts:
            if name == card['name']: # case sensitive due to the importance of delete function
                contacts.remove(card) # .remove() deletes contact with input name
                break
        else:
            print('No contact found.')
    elif command == 'list':
        for card in contacts:
            print(card['name']) # contact name as listed in JSON plus below JSON info formatted
            print('    Age:', card['age'], '    e-mail:', card['email'], '    Favorite color:', card['favorite color'])
    elif command == 'save': #saves on command 'save'
        save_contacts(path, contacts) # function defined above
    else:
        print('Command not recognized.') # if invalid command enterd above

save_contacts(path, contacts) # saves changes to the file only after exit
       




'''
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
'''