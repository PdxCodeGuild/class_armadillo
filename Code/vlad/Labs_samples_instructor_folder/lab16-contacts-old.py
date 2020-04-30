
#lab16-contacts-old by instructor

import json 

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


def print_contact(contact):
  print(contact['name'])
  print('  Age:', contact['age'])
  print('  Email:', contact['email'])
  print('  Favorite Color: ', contact['favorite color'])


# maybe write a function for this?
# def create_contact(contacts):
#   # prompt the user for the contact's values
#   name = input('What is the contact\'s name? ')
#   age = int(input('What is the contact\'s age? '))
#   email = input('What is the contact\'s email? ')
#   favorite_color = input('What is the contact\'s favorite color? ')
#   # append the new contact to the list
#   contacts.append({
#     'name': name,
#     'age': age,
#     'email': email,
#     'favorite color': favorite_color
#   })

# loading the contacts from the file
path = 'contacts.json'
contacts = load_contacts(path)

while True:
  command = input('what is your command? ')
  if command in ['done', 'exit', 'quit']:
    break
  elif command == 'create':
    # prompt the user for the contact's values
    name = input('What is the contact\'s name? ')
    age = int(input('What is the contact\'s age? '))
    email = input('What is the contact\'s email? ')
    favorite_color = input('What is the contact\'s favorite color? ')
    # append the new contact to the list
    contacts.append({
      'name': name,
      'age': age,
      'email': email,
      'favorite color': favorite_color
    })
  elif command == 'retrieve':
    name = input('What is the contact\'s name? ')
    found_contact = False
    for contact in contacts:
      # if contact['name'] == name:
      # check if what the user entered is in the contact's name
      if name.lower() in contact['name'].lower():
        print_contact(contact)
        found_contact = True
    if not found_contact:
      print('no contact found with that name')
  elif command == 'update':
    name = input('What is the contact\'s name? ')
    for contact in contacts: # loop over the contacts
      if contact['name'] == name: # if the contact's name matches the entered name
        # prompt the user for their new attributes
        name = input('What is the contact\'s new name? ')
        age = int(input('What is the contact\'s new age? '))
        email = input('What is the contact\'s new email? ')
        favorite_color = input('What is the contact\'s new favorite color? ')
        # replace the old attributes with the new ones
        contact['name'] = name
        contact['age'] = age
        contact['email'] = email
        contact['favorite color'] = favorite_color
        break
    else:
      print('no contact found with that name')
  elif command == 'delete':
    name = input('What is the contact\'s name? ')
    for contact in contacts:
      if contact['name'] == name:
        contacts.remove(contact)
        break
    else:
      print('no contact found with that name')
  elif command == 'list':
    for contact in contacts:
      print_contact(contact)
  elif command == 'save':
    save_contacts(path, contacts)
  else:
    print('command not recognized')

# saving our contacts to the file
save_contacts(path, contacts)