#Implement a CRUD REPL

# create a record and ask user for attributes to create list for user to enter.

user = input("I'm going to create contact info for you.  Can you provide me with some information please?" )


name = input("What is your name? :")
age = input("What is your age? :")
email = input("What is your email address? :")
color = input("What is your favorite color? :")

#```python
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