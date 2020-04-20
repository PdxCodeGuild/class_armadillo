import json
path = 'contacts.json'


def load_contacts(path):
    with open(path, 'r') as file:
        text = file.read()
    contacts = json.loads(text)
    return contacts


def save_contacts(path, contacts):
    with open(path, 'w') as file:
        text = json.dumps(contacts, indent=4, sort_keys=True)
        file.write(text)


contacts = load_contacts(path)
run = True
valid_operation = False

while run:

    print('''Welcome to Contact Manager 5000(tm)!
    Current operations are: create, retrive, update, delete, and list.
    ''')
    while not valid_operation:
        operation = input("What operation should I perform? ").lower().strip()

        if operation == "create":
            name = input("Enter contacts name.")
            age = input("Enter contacts age.")
            email = input("Enter contacts email.")
            color = input("Enter contacts favorite color.")
            new = {"name": name, "age": age, "email": email, "color": color}
            contacts.append(new)
            print("New contact added!")
            print(contacts)
            save_contacts(path, contacts)
            valid_operation = True
            run = False
        elif operation == "retrive":
            retrieve_name = input("Whose info would you like? ").strip()
            for contact in contacts:
                if contact["name"] == retrieve_name:
                    print("Here is that info:")
                    print(contact)
            valid_operation = True
            run = False
        elif operation == "update":
            print(contacts)
            to_update = input("Whose info needs updated? ")
            for contact in contacts:
                if contact["name"] == to_update:
                    print(contact)
                    update_field = input("What needs changed? ")
                    for field in contact:
                        if field == update_field:
                            contact[field] = input("What's the new value? ")
                            print("Contact has sucessfull been updated!")
                            print(contact)
            save_contacts(path, contacts)
            valid_operation = True
            run = False

        elif operation == "delete":
            print(contacts)
            to_delete = input("Whose info needs deleted? ")
            for contact in contacts:
                if contact["name"] == to_delete:
                    check = input("Are you sure you want to delete? (Y/N) ")
                    if check == "Y":
                        contacts.remove(contact)
                        print("User has sucessfull been removed.")
            save_contacts(path, contacts)
            valid_operation = True
            run = False

        elif operation == "list":
            print(contacts)
            valid_operation = True
            run = False
        else:
            print("please enter a valid operation.")

    while not run:
        checkin = input("Do you have additional operations? (Y/N) ")
        if checkin == "Y":
            valid_operation = False
            run = True
            break
        elif checkin == "N":
            print("Thank you for using Contact Master 5000!")
            exit()
        else:
            print("Please enter a valid response.")
