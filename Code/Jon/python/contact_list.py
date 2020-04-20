import json

# JSON should enclosed in a dictionary
# some json parsers will crash if you just have a list

# Works
# Changes JSON file list into a dictionary
def load_contacts():
    with open(r'python\contacts.json', 'r') as file:
        text = file.read()
    contacts = json.loads(text)
    return contacts

# Works
# saves changes
def save_contacts(contacts):
    with open(r'python\contacts.json', 'w') as file:
        text = json.dumps(contacts)
        file.write(text)

#  Works
# creates new object
def create(contacts):
    name = input('Please enter a name: ')
    age = int(input('Please enter in an age: '))
    email = input('Please enter in an email: ')
    fav_color = input('Please enter in a favorite color: ')

    # Can't figure out how to push this
    contacts['contacts'].append({
        'name': name,
        'age': age,
        'email': email,
        'favorite color': fav_color
    })
    return contacts

# Works
# Reads a specific object
def read(contacts):
    user_query = int(input(f"Which contact would you like to view? (0-{len(contacts['contacts'])-1}): "))
    print(f"{contacts['contacts'][user_query]['name']}, {contacts['contacts'][user_query]['age']}, {contacts['contacts'][user_query]['email']}, {contacts['contacts'][user_query]['favorite color']}")

# Works
def update(contacts):
    name = input('Please enter a name: ')
    age = int(input('Please enter in an age: '))
    email = input('Please enter in an email: ')
    fav_color = input('Please enter in a favorite color: ')

    user_update = int(input(f'Which contact would you like to update? (0-{len(contacts["contacts"])-1}): '))
    contacts['contacts'][user_update].update({'name': name,'age': age, 'email': email, 'favorite color': fav_color})

    return contacts

# Works
# Destroys specific object
def destroy(contacts):
    user_query = int(input(f'Which contact would you like to destroy? (0-{len(contacts["contacts"])-1}): '))
    contacts['contacts'].pop(user_query)
    return contacts

# Works
# Lists all objects
def list_contacts(contacts):
    list_num = 0
    for contact in contacts['contacts']:
        print(f'{list_num}. {contact}')
        list_num += 1

# Runs loop
def main(contacts):
    print('Welcome to the JSON editor.\nYou will be able to use CRUDle to edit the JSON file.')

    main_loop = True
    while main_loop:
        user_decision = input('Would you like to Create, Read, Update, Destroy, List or done: ').lower()
        if user_decision == 'create':
            create(contacts)
            save_contacts(contacts)
        elif user_decision == 'read':
            read(contacts)
        elif user_decision == 'update':
            update(contacts)
            save_contacts(contacts)
        elif user_decision == 'destroy':
            destroy(contacts)
            save_contacts(contacts)
        elif user_decision == 'list':
            list_contacts(contacts)
        
        if user_decision != 'done':
            continue
        else:
            print('Goodbye!')
            main_loop = False

main(load_contacts())

# start_json = load_contacts()
# print(start_json['contacts'][0]['name'])