import json

path = 'contacts.json'
with open(path, 'r') as file:
  text = file.read()
print(text)

def load_contacts(path):
    with open(path, 'r') as file: # open the file
        text = file.read() # read the text out of the file
    contacts = json.loads(text) # convert the text containing json into a dictionary
    contacts = contacts['contacts'] # extract the list inside the dictionary
    return contacts

def save_contacts(path, contacts):
    contacts = {'contacts': contacts} # put the list of contacts in to a dictionary
    with open(path, 'w') as file: # open the file
        text = json.dumps(contacts, indent=4, sort_keys=True) # convert our list of dictionaries into json
        file.write(text) # write the json to the file

def create(path, contacts):
    contact_name = input("What is the contact name? ")
    contact_phone = input("What is the contact phone number? ")
    contact_email = input("What is the contact email? ")
    contact_bday = input("What is the contact birthday? ")

    created_dictionary = {contact_name + contact_phone + contact_email + contact_bday}

    return created_dictionary

# loading the contacts from the file
path = 'contacts.json'
contacts = load_contacts(path)

# print(contacts)
# print(type(contacts))

# print(contacts[0]['name'])
# print(contacts['contacts'][0]['name'])


while True:
  command = input('what is your command? ')
  if command in ['done', 'exit', 'quit']:
    break
  elif command == 'create':
    create(path, contacts)
  elif command == 'retrieve':
      pass
  elif command == 'update':
      pass
  elif command == 'delete':
      pass
  elif command == 'list':
      for contact in contacts:
        print(' age:'. contact['age'])
        print(' email:')
  else:
    print('command not recognized')

# saving our contacts to the file
save_contacts(path, contacts)


'''
Lab 16: Contact List
Let's build a program to manage a list of contacts, using a JSON file. Create a text file in the same folder as your lab, paste the following content, and save it as "contacts.json".

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
Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'joe', 'age': 34, 'email': 'joe@gmail.com', 'favorite color':'blue'},
    {'name':'jane', 'age': 43 ...}
]
Then implement the following operations in a REPL:

Create a contact: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a contact: ask the user for the contact's name, find the user with the given name, and display their information
Update a contact: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a contact: ask the user for the contact's name, remove the contact with the given name from the contact list.
List a contact: list all the contacts and their information
Exit: save the contacts to a file and exit the program
Example run:

Welcome to the Contact Manager 5000(tm)!
What operation would you like to perform? create
What is the contact's name? Bob
What is the contact's age? 56
What is the contact's email? bob@email.com
What is the contact's favorite color? blue
Contact Bob has been added!
What operation would you like to perform?

'''