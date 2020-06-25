
import json

def load_database():
    with open('db.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_database(data):
    with open('db.json', 'w') as file:
        file.write(json.dumps(data, indent=4, sort_keys=True))

data = load_database()
print(data)
print(data['value'])
data['value'] += 1

print(data)

save_database(data)
