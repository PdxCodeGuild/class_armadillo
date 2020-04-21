Implement a CRUD REPL

# create a record and ask user for attributes to create list for user to enter.

user = input("I'm going to create contact info for you.  Can you provide me with some information please?" )

user = input("Can you provide me with your name, age, email, and favorite color, please? ")

```python
import json

def load_data():
    with open('contacts, json', 'r') as file:   contacts= json.
with open('contacts.csv', 'r') as file:
    lines = file.read(). split('\n')
    print(lines)
```

{
        "contacts": [{
            "name": "joe",
            "age": 34,
            "email": "joe@gmail.com",
            "favorite color": "blue"},{"name": "jane", "age":"43" ...}
        
]
```

contact = [
    {"name": "joe", "age": "34", "email": joe@gmail.com", "favorite color": "blue"}, {"name": "jane", "age": "43" ...}
]





{"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
]}


import json
person = {'name': 'jane', 'age': 34} # python dictionary
json_person = json.dumps(person) # convert a dictionary to a string containing json
person = json.loads(json_person) # convert a string containing json to a dictionary
let person = {name: 'jane', age: 34} // javascript object
let json_person = JSON.stringify(person) // convert a javascript object into a string containing json
person = JSON.parse(json_person) // convert a string containing json into a javascript object