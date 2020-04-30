#in this lab we manage a contact list using a JSON file

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
        text = json.dumps(contacts, indent=4, sort_keys=True) # convert our list of dictionaries into json, #indent formats
        file.write(text) # write the json to the file


# loading the contacts from the file
path = 'contacts.json'
contacts = load_contacts(path)

while True:
  command = input('what is your command? ') # takes command from user
  if command in ['done', 'exit', 'quit']:  #ends loop, saves info
    break
  elif command == 'create':  #add new contact
      name = input('What is the name of the contact you would like to create?: ')  #user inputs
      age = int(input('What is the contact\'s age?: ')) 
      email = input('What is the contact\'s e-mail address?: ')
      favorite_color = input('What is the contact\'s favorie color?: ') 
      new_contact = {  #creates dictionary for new contact
        'name' : name,
        'age' : age,
        'email' : email,
        'favorite color' : favorite_color, 
    } 
      contacts.append(new_contact) #adds new contact info
  elif command == 'retrieve':  #recalls current contact from JSON file
      retrieve_contact = input('What is the name of the contact you would like to retrieve?: ')    
      for contact in contacts: #loop over contacts
          if contact['name'] == retrieve_contact:  #if contacts name matches input
            print(contact['name'])  #prints data from lists
            print('Age:', contact['age'])
            print('Email:', contact['email'])
            print('Favorite Color:', contact['favorite color'])
  elif command == 'update':  #alters current contact
      name = input('Which contact would you like to update?') #user enters name
      for contact in contacts:  #loops over contacts
          if contact['name'] == name:  
            name = input('What is the updated name of the contact you would like to create?: ')
            age = int(input('What is the contact\'s updated age?: ')) 
            email = input('What is the contact\'s updated e-mail address?: ')
            favorite_color = input('What is the contact\'s new favorite color?: ')
            contact['name'] = name  #add new inputs to dictionary in JSON file
            contact['age'] = age
            contact['email'] = email
            contact['favorite color'] = favorite_color
  elif command == 'delete':  #removes contact
      delete_contact = input('Which contact would you like to delete?: ')  #user selects contact to remove
      for contact in contacts:
          if contact['name'] == delete_contact:
              contacts.remove(contact)  #removes contact
  elif command == 'list':  #retrieves entire list of contacts in file
      for contact in contacts:  
        print('name:', contact['name'])
        print('age:', contact['age'])
        print('email:', contact['email'])
        print('favorite_color:', contact['favorite color'])
          
  else:  #if user enters invalid command
    print('command not recognized')

# saves contacts to JSON file
save_contacts(path, contacts)