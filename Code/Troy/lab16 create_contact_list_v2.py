import json

def load_contacts(file_name):

    with open(file_name, 'r') as contacts_file:
        contacts = contacts_file.read()

        contacts = json.loads(contacts)
    return contacts['contacts']

def create_contact():
    name = input('What is the contact\'s name?\n')
    age = int(input('What is the contact\'s age?\n'))
    email = input('What is the contact\'s email?\n')
    favorite_color = input('What is the contact\'s favorite color?\n')

    new_contact = {
        'name': name,
        'age': age,
        'email': email,
        'favorite color': favorite_color  
    }

    return new_contact

def retrieve(find_key):
    pass


file_name = 'contacts.json'
contacts = load_contacts(file_name)
# new_contact = create_contact() 
# print(contacts) 
# contacts.append(new_contact)
# print(new_contact)
# print(contacts)

while True:
    function = input('What operation would you like to do? ')
    if function == 'create':
        print('You chose create a contact.')

    elif function == 'retrieve':
        print('You chose retrieve a contact.')
    elif function == 'update':
        print('You chose update a contact.')
    elif function == 'delete':
        print('You chose delete a contact.')
    elif function == 'list':
        print('You chose list a contact.')
    elif function == 'exit':
        print('You chose exit a contact.')
    else:
        print('Please enter a valid function.')
        continue


    