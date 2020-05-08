# Lab 16



import json

#function with 2 --parameters
def find_contact(name, contacts):
  for contact in contacts:             #method
    if name.lower() == contact['name'].lower():
      return contact
  return None


with open('contacts.json', 'r') as file:
  text = file.read()
data = json.loads(text)
contacts = data['contacts']



# REPL - read evaluate print loop
# CRUDL - create retrieve update delete list
while True:
  command = input('what is your command? ') # get the command from the user

  # CREATE CONTACT
  if command == 'create':
    # get the new contact's information from the user
    name = input('what is the contact\'s name? ')
    age = int(input('what is the contact\'s age? '))
    email = input('what is the contact\'s email? ')
    fav_color = input('what is the contact\'s favorite color? ')
    # create a new contact as a dictionary
    contact = {
      'name': name,
      'age': age,
      'email': email,
      'favorite color': fav_color
    }
    # add the new contact to our list of contacts
    contacts.append(contact)

  # RETRIEVE CONTACT
  elif command == 'retrieve':
    name = input('what is the contact\'s name which you are looking for? ')
    contact = find_contact(name, contacts)
    if contact is None:
      print('contact not found')
    else:
      # print(contact)
      print(contact['name'])
      print('  Age: ' +str(contact['age']))
      print('  Email: ' + contact['email'])
      print('  Favorite Color: ' + contact['favorite color'])

  # UPDATE CONTACT
  elif command == 'update':
    name = input('what is the contact\'s name which you want to update? ')
    field = input('what field would you like to update? (name, age, email, favorite color)? ')
    value = input('what is the new value? ')
    contact = find_contact(name, contacts)
    if contact is None:
      print('contact not found')
    else:
      contact[field] = value

  # DELETES CONTACT
  elif command == 'delete':
    name = input('what is the contact\'s name which you want to delete? ')
    contact = find_contact(name, contacts)
    if contact is None:
      print('contact not found')
    else:
      contacts.remove(contact)
    
  # LISTS CONTACT
  elif command == 'list':
    for contact in contacts:
      print(contact['name'])
      print('  Age: ' +str(contact['age']))
      print('  Email: ' + contact['email'])
      print('  Favorite Color: ' + contact['favorite color'])
  elif command == 'exit':
    break
  else:
    print('command not recognized')


# write our list of contacts back into contacts.json
text = json.dumps({'contacts': contacts}, indent=4)
with open('contacts.json', 'w') as file:
  file.write(text)


