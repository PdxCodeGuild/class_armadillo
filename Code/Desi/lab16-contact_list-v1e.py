

```json
{
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
```




```python
import json

def load_data():
    with open('contacts.json', 'r') as file:
        contacts=  json.
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
```

Once you've processed the file, your list of contacts will look something like this...
```python
contacts = [
    {'name':'joe', 'age': '34', 'email': 'joe@gmail.com', 'favorite color':'blue'},
    {'name':'jane', 'age':'43' ...}
]
```

## Version 2

Implement a CRUD REPL

- **C**reate a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
- **R**etrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
- **U**pdate a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
- **D**elete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

## Version 3

When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup `contacts.csv` because you likely won't write it correctly the first time.

