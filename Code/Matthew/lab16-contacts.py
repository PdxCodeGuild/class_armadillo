

import json 
# path = r'C:\Users\flux\programs\class_armadillo\Code\Matthew\contacts.json'
# path = 'contacts.json'
# with open(path, 'r') as file:
#   text = file.read()
# print(text)

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
    contacts.append({'name':'john'})
  else:
    print('command not recognized')

# saving our contacts to the file
save_contacts(path, contacts)