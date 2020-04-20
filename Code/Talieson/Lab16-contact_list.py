import json
path = r'Code\Talieson\data\contacts.json'


# Main function to read the json file
def load_contacts(path):
    # open the file as text
    with open(path, 'r') as file:
        text = file.read()
    # store that text inside a list
    contacts = json.loads(text)
    # extract the list inside the dictionary to make a list of dictionaries
    contacts = contacts["contacts"]
    return contacts


# Write to our json file
def save_contacts(path, contacts):
    # Convert list of dictionaries to a dictionary of lists of dictionaries
    contacts = {'contacts': contacts}
    with open(path, 'w') as file:
        # set local variable text to the output of contacts and save it to json
        text = json.dumps(contacts, indent=4)
        file.write(text)


# The contents of the json gathered from load function is stored here.
contacts = load_contacts(path)
# Global variables.
run = True

# Main run loop.
while run:
    print()
    print('''        Welcome to Contact Manager 5000(tm)!
        Current operations are: create, retrive, update, delete, and list.
''')
    # Take users operation here.
    operation = input("What operation should I perform? ").lower().strip()
    print()
    # Check if operation is create. if so, store pertainate info in variables.
    if operation == "create":
        name = input("Enter contacts name. ").capitalize()
        age = int(input("Enter contacts age. "))
        email = input("Enter contacts email. ").lower()
        color = input("Enter contacts favorite color. ").lower()
        # Create a dictionary from the variables and add it to contacts.
        new = {"name": name, "age": age, "email": email, "color": color}
        contacts.append(new)
        # Print sucess message, show the added info, and save to JSON file.
        print("New contact added!")
        print(new)
        save_contacts(path, contacts)
        # Exit main run loop.
        run = False
    # Check if operation is retrieve. Get name of retieve-ee.
    elif operation == "retrive":
        print(contacts)
        print()
        # start with a false name to enable validation
        retrieve_name = False
        while retrieve_name is False:
            retrieve_name = input("Whose info would you like? ").strip()
            # iterate through list of contacts and get contact with that name.
            for contact in contacts:
                if contact["name"] == retrieve_name:
                    print("Here is that info:")
                    print(contact)
                    break
            # if we don't find it, print error and set retrieve_name to false.
            else:
                print('''
        I'm sorry. that name is not inside Contact Manger 5000(tm).
                ''')
                retrieve_name = False
        # Exit main run loop.
        run = False
    # Check if operation is up. Dispaly info and get name of update-ee.
    elif operation == "update":
        print(contacts)
        to_update = input("Whose info needs updated? ")
        # if we find that contact check the field that needs updating.
        for contact in contacts:
            if contact["name"] == to_update:
                print(contact)
                update_field = input("What needs changed? ")
                # check each field in contact.
                for field in contact:
                    # if we find that field, set it to input value.
                    if field == update_field:
                        contact[field] = input("What's the new value? ")
                        # print a success message and show new contact info.
                        print("Contact has sucessfully been updated!")
                        print(contact)
        # save changes and exit run loop
        save_contacts(path, contacts)
        run = False

    # check if operation is delete, and show contacts.
    elif operation == "delete":
        print(contacts)
        # Get name of delete-ee, check contacts for it.
        to_delete = input("Whose info needs deleted? ")
        for contact in contacts:
            # if we find it, make extra sure they want it deleted.
            if contact["name"] == to_delete:
                check = input('''
        Are you sure you want to delete this contact from Contact Manager 5000?
        if so, type YES. Otherwise, enter any key.
                ''').strip()
                if check == "YES":
                    # if they're sure, remove it, display success message.
                    contacts.remove(contact)
                    print("Contact has sucessfully been removed.")
                else:
                    print("Contact information unchanged.")
        # save changes and exit run loop
        save_contacts(path, contacts)
        run = False

    # if operation is list, print the contacts and exit run loop.
    elif operation == "list":
        print(contacts)
        run = False
    # if it's nto any of the functions, display error message.
    else:
        print("please enter a valid operation.")

    # check if need to run again.
    while not run:
        checkin = input("Do you have additional operations? (Y/N) ")
        if checkin == "Y":
            run = True
        elif checkin == "N":
            print('''
            Thank you for using Contact Master 5000!
            ''')
            exit()
        else:
            print("Please enter a valid response.")
