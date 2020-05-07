import json

# data types you can store in json
# None, bool, int, float, string, list, tuple, dict

# serializing a python dictionary into json
# json.dumps({"range": range(10)}) TypeError: Object of type range is not JSON serializable
person = {"people":[{'name': 'jane', 'age': 34}], "count": ('hi', 'there')} # python dictionary
json_person = json.dumps(person) # convert a dictionary to a string containing json

# loading json into a python dictionary
person_json = '{"name":"ja\'ne", "age": 34}'
person = json.loads(person_json)
# print(person)
# print(person['name'])


# if I hit the green > button it runs from the repo directory
# path = 'Code/Matthew/demos/test1.txt'

# cd into the same directory as the .py file and run it using python <file>
# path = 'test1.txt'

# absolute paths won't work on other computers
# path = r'C:\Users\flux\programs\class_armadillo\Code\Matthew\demos\test1.txt'

# example using relative path
# path = '../data/test.txt'

path = 'test1.txt'
with open(path, 'r') as file:
  # text = file.read() # read contents of file as one big string
  # lines = file.readlines() # read all the lines in the file, gives a list of string
  lines = file.read().split('\n') # better way?
  # for line in file:
  #   print(line)


# print(text)
# print(lines)

# passing 'w' to open and calling write will replace text
fruits = ['apples', 'bananas', 'cherries', 'avocados']
with open(path, 'w') as file:
    file.write('\n'.join(fruits))

# passing 'a' to open and calling write will append text
# the name 'file' is arbitrary
with open(path, 'a') as llama:
    llama.write('hello world!')



contacts = {
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
print(contacts['contacts'][0]['name']) # Joe
print(json.dumps(contacts, indent=4, sort_keys=True))

# JSON should enclosed in a dictionary
# some json parsers will crash if you just have a list
print(json.dumps(['a', 'b', 'c']))
print(json.loads('["a","b","c"]'))

def load_contacts():
    with open('contacts.json', 'r') as file:
        text = file.read()
    contacts = json.loads(text)
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        text = json.dumps(contacts)
        file.write(text)