#Lab 16: Contact List


# import json

# with open('contacts.json', 'r') as contacts_archi:
#     contacts = contacts_archi.read()

#     print(contacts)
#     contacts = json.loads(contacts)
#     print(contacts)
#     print(type(contacts))


   
#Example run:
# print('Welcome to the Contact Manager 5000(tm)!')
# user_input = input('What operation would you like to perform?')
# user_input = input('What is the contact name?')
# user_input = int(input('What is the contact age'))
# # user_input = input(What is the contact's email? bob@email.com
# # user_input = input(What is the contact's favorite color? blue
# # user_input = input(Contact Bob has been added!
# # user_input = input(What operation would you like to perform?




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

def print_contact(contact):
    print(contact['name'])
    print('  Age:', contact['age'])
    print('  Email:', contact['email'])
    print('  Favorite  Color:', contact['color'])

# loading the contacts from the file
path = 'contacts.json'
contacts = load_contacts(path)

# print(contacts)
# print(type(contacts))

# print(contacts[0]['name'])
# print(contacts['contacts'][0]['name'])

#
print('Welcome Contact Manager :)!')
while True:
    command = input('what is your command? please type one of the following: create or retrieve or update or delete or done, exit, quit - Please type one:  ')
    if command in ['done', 'exit', 'quit']:
        break
    
    if command == 'create':
        name = input('What is the contact name? ')
        age = input('What is the contact age? ')
        email = input('What is the contact email? ')
        color = input('What is the contact favorite color? ')
    
        new_contact = {
            
            'name': name,
            'age': age,
            'email': email,
            'color': color,
        }
        contacts.append(new_contact)

    elif command == 'retrieve':
        name = input('What is the contact name to retrieve? ')
        found_it = False
        for contact in contacts:
            if name == contact['name']:
                print_contact(contact)
            found_it = True 
        if contact not in contacts:
                print('Sorry no contact found try different name')

    elif command == 'update':
        """
                Update a contact: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
        """
        name = input('What is the contact name to update? ')
        

        found_it = False
        for contact in contacts:
            if name == contact['name']:
                attribute = input('What would you like to update ')
                attribute2 = input('update to: ')
                if attribute in contact:
                    contact[attribute] = attribute2
            found_it = True 
        if contact not in contacts:
                print('Sorry no contact found try different name')


    elif command == 'delete':
       """ 
            Delete a contact: ask the user for the contact's name, remove the contact with the given name from the contact list.
       """
    name = input('What is the contact name to delete? ')
   
    for contact in contacts:
            if name == contact['name']:
                #contacts.del(contact) 
                #ask how to use del()  ?
                #ask why it is promptying for delete after enter the name to delete

                contacts.remove(contact)
                break
    else:
        print('contact name not recognized')

# saving our contacts to the file
save_contacts(path, contacts)



# # import json

# # data types you can store in json
# # None, bool, int, float, string, list, tuple, dict

# # serializing a python dictionary into json
# # json.dumps({"range": range(10)}) TypeError: Object of type range is not JSON serializable
# person = {"people":[{'name': 'jane', 'age': 34}], "count": ('hi', 'there')} # python dictionary
# json_person = json.dumps(person) # convert a dictionary to a string containing json

# # loading json into a python dictionary
# person_json = '{"name":"ja\'ne", "age": 34}'
# person = json.loads(person_json)
# # print(person)
# # print(person['name'])


# # if I hit the green > button it runs from the repo directory
# # path = 'Code/Matthew/demos/test1.txt'

# # cd into the same directory as the .py file and run it using python <file>
# # path = 'test1.txt'

# # absolute paths won't work on other computers
# # path = r'C:\Users\flux\programs\class_armadillo\Code\Matthew\demos\test1.txt'

# # example using relative path
# # path = '../data/test.txt'

# # path = 'test1.txt'
# # with open(path, 'r') as file:
# #   # text = file.read() # read contents of file as one big string
# #   # lines = file.readlines() # read all the lines in the file, gives a list of string
# #   lines = file.read().split('\n') # better way?
# #   # for line in file:
# #   #   print(line)


# # # print(text)
# # # print(lines)

# # # passing 'w' to open and calling write will replace text
# # fruits = ['apples', 'bananas', 'cherries', 'avocados']
# # with open(path, 'w') as file:
# #     file.write('\n'.join(fruits))

# # # passing 'a' to open and calling write will append text
# # # the name 'file' is arbitrary
# # with open(path, 'a') as llama:
# #     llama.write('hello world!')



# # contacts = {
# #     "contacts": [{
# #         "name": "Joe",
# #         "age": 34,
# #         "email": "joe@email.com",
# #         "favorite color": "blue"
# #     },{
# #         "name": "Jane",
# #         "age": 43,
# #         "email": "jane@email.com",
# #         "favorite color": "green"
# #     },{
# #         "name": "Jill",
# #         "age": 65,
# #         "email": "jill@email.com",
# #         "favorite color": "orange"
# #     }]
# # }
# # print(contacts['contacts'][0]['name']) # Joe
# # print(json.dumps(contacts, indent=4, sort_keys=True))

# # # JSON should enclosed in a dictionary
# # # some json parsers will crash if you just have a list
# # print(json.dumps(['a', 'b', 'c']))
# # print(json.loads('["a","b","c"]'))

# # def load_contacts():
# #     with open('contacts.json', 'r') as file:
# #         text = file.read()
# #     contacts = json.loads(text)
# #     return contacts

# # def save_contacts(contacts):
# #     with open('contacts.json', 'w') as file:
# #         text = json.dumps(contacts)
# #         file.write(text)