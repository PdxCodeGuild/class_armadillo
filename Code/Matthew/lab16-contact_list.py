

import json





def find_contact(name, contacts):
  for contact in contacts:
    if name.lower() == contact['name'].lower():
      return contact
  return None


# file = open('contact.json', 'r')
# text = file.read()
# # ....
# file.close()

# File I/O Doc
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/docs/11%20-%20FileIO.md
with open('contacts.json', 'r') as file:
  text = file.read()


# dictionaries
# keys can be any immutible type - bools, int, float, string, tuples
# values can be any type
# fruits = {'apples': 1.0, 'bananas': 2.0, 'cherries': 3.0}
# print(fruits['apples']) # 1.0
# fruits['bananas'] = 2.5

# # loading json into a python dictionary
# myjson = '{"name":"joe"}' # string containg json
# data = json.loads(myjson) # load json into a python dictionary
# print(data['name']) # access and print out a value from the dictionary using a key
# data['name'] = 'jane' # set a new value for the key 'name'
# myjson = json.dumps(data) # turn the python dictionary back into a json string
# print(myjson) # print the json string



# types of data you can store in json
# python - None, bool, int, float, string, list, dictionary
# json   - null, bool, int, float, string, arrays, objects
# json should always be enclosed in a dictionary

data = json.loads(text)
# print(data)
# print(data['contacts'][1]['favorite color']) # green

contacts = data['contacts']


# REPL - read evaluate print loop
# CRUDL - create retrieve update delete list
while True:
  command = input('what is your command? ') # get the command from the user
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
  elif command == 'update':
    name = input('what is the contact\'s name which you want to update? ')
    field = input('what field would you like to update? (name, age, email, favorite color)? ')
    value = input('what is the new value? ')
    contact = find_contact(name, contacts)
    if contact is None:
      print('contact not found')
    else:
      contact[field] = value
  elif command == 'delete':
    name = input('what is the contact\'s name which you want to delete? ')
    contact = find_contact(name, contacts)
    if contact is None:
      print('contact not found')
    else:
      contacts.remove(contact)
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


