import json

print('\n')
print('=======================================')
print('Welcome to the Contact Manager 5000(tm)!')
print('=======================================')
print('\n')

path = 'contacts.json'


def load_contacts(path):
    with open(path, 'r') as file:
        text = file.read()
    contacts = json.loads(text)
    contacts = contacts['contacts']
    return contacts

def save_contacts(path, contacts):
    contacts = {'contacts': contacts}
    with open(path, 'w') as file:
        text = json.dumps(contacts, indent=4, sort_keys = True)
        file.write(text)

def print_contact(contact):
  print(contact['name'])
  print('  Age:', contact['age'])
  print('  Email:', contact['email'])
  print('  Favorite Color: ', contact['favorite color'])
  
# loading the contacs from the file
path = 'contacts.json'
contacts = load_contacts(path)

# print(contacts)
# print(contacts['contacts'][0]['name'])
while True:
    command = input('What operation do you want to perform? ')
    if command in ['done', 'exit', 'quit']:
        print("GoodBye")
        break

    elif command == 'create':
        name = input('Whats your contacts name? ')
        age = int(input("Whats your contacts age? "))
        email = input("Whats your contacts email? ")
        color = input("Whats your favorite color ")
        # append the new contact to the list
        contact = {
            'name': name,
            'age' : age,
            'email': email,
            'favorite_color': color,
        }
        contacts.append(contact)
        print(contact)
        save_contacts(path, contacts)

    elif command == 'retrive':
        name = input('What is your contact name? ')
        found_contact = False
        for contact in contacts:
            if name.lower() in contact['name'].lower():
                print_contact(contact)
                found_contact = True
        if not found_contact:
            print('no contact with that name ')

    elif command == 'update':
        name = input('What is your contact name? ')
        for contact in contacts:
            if contact['name'] == name:

                name = input('Whats your contacts name? ')
                age = int(input("Whats your contacts age? "))
                email = input("Whats your contacts email? ")
                favorite_color = input("Whats your favorite color ")
                contact['name'] = name
                contact['age'] = age
                contact['email'] = email
                contact['favorite_color'] = favorite_color
                save_contacts(path, contacts)
                break
        else:
            print('no contact found with that name')

    elif command == 'delete':
        print(contacts)
        name = input('What contact do you want to delete? ')
        for contact in contacts:
            if contact['name'] == name:
                making_sure = input('Are you sure you want to delete? ')
                if making_sure == 'yes':
                    contacts.remove(contact)
                    save_contacts(path, contacts)
                    print('Your contact has been deleted ')
                else:
                    print("Contact unchanged")

                


    elif command == 'list':
        for contact in contacts:
            print(contact['name'])
            print(contact['age'])
    else:
        print('command not regognized')
# #saving our contacts
save_contacts(path, contacts)


