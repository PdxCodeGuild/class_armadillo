import json

path = 'contacts.json'

with open(path, 'r') as file:
    text = file.read()


def load_contacts(contacts):
    with open('contacts.json', 'r') as file:
        text = file.read()
    contacts = json.loads(text)
    contacts = contacts['contacts']
    return contacts

def save_contacts(path, contacts):
    contacts = {'contacts': contacts} # put the list of contacts in to a dictionary
    with open(path, 'w') as file: # open the file
        text = json.dumps(contacts, indent=4, sort_keys=True) # convert our list of dictionaries into json
        file.write(text) # write the json to the file


contacts = load_contacts(path)
print(contacts)

# print(contacts[0]['name'])


while True:
    command = input('\nWelcome to the Contact Dominator 9001!\n \nWhat operation would you like to perform? ')
    if command in ['done', 'finished', 'quit', 'exit']:
        break
    elif command == 'create':
        name = input('What is the contact\'s name? ')
        age = input('What is the contact\'s age? ')
        email = input('What is the contact\'s email? ')
        color = input('What is the contact\'s favorite color? ')
        contacts.append({'name':name, 'age':age, 'email':email, 'favorite color':color})
        print(f'Contact {name} has been added!')
        print(contacts)
    elif command == 'retrieve':
        name = input('Who do you want to look up? ')
        print(name)
    elif command == 'list':
        name = input('What is the contact\'s name')
        found_contact = False
        for contact in contacts:
            if name.lower() in contact['name'].lower():
                print_contact(contact)
                found_contact = True
    elif command == 'update':
        name = input('what is the contact\'s name which you want to update? ')
        field = input('what field would you like to update? (name, age, email, favorite color)? ')
        value = input('what is the new value? ')
        for contact in contacts:
            if contact['name'] == name:
                contact[field] == 'name'
    else:
        print('command not recognized')
        break

save_contacts(path, contacts)