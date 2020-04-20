import json

# Loads the contacts from a file that is located in the local directory.
def load_contacts():
    with open('contacts.json', 'r') as file:
        text = file.read()
    contacts = json.loads(text)["contacts"]
    return contacts

# Saves the contacts to a faile that is located in the local directory.
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        text = json.dumps(contacts)
        file.write(text)

# Prints the list of contacts
def print_contacts(contacts):
    print("------------------------------ Contact List ------------------------------")
    print("Name:\t\tAge:\t\tEmail:\t\t\tFavorite Color:\t\t")
    # For each contact in the contact list, loop.
    for contact in contacts:
        print(contact["name"] + "\t\t" + str(contact["age"])+ "\t\t" + contact["email"] + "\t\t" + contact["favorite color"] + "\t\t")

# Deletes a contact in the contacts dictionary based on the string that was used as an input.
def delete_contact(contacts, contact_to_remove):
    # For each contact in the contact list, loop.
    for contact in contacts:
        if contact["name"] == contact_to_remove:
            contacts.remove(contact)
            return contacts

# Prints a specific contact based on the string that was used as an input.
# Returns True if the contact was in the dictionary.
# Returns False if the contact was not in the dictionary.
def print_specific_contact(contacts, contact_to_print):
    # For each contact in the contact list, loop
    for contact in contacts:
        if contact["name"] == contact_to_print:
            print("-------------------------------- Contact ---------------------------------")
            print("Name:\t\tAge:\t\tEmail:\t\t\tFavorite Color:\t\t")
            print(contact["name"] + "\t\t" + str(contact["age"])+ "\t\t" + contact["email"] + "\t\t" + contact["favorite color"] + "\t\t")
            return True
    print("The contact you entered is not in the list, please try again.")
    return False

# Updates a contact in the contact dictionary based on the string that was used as an input.
def update_contact(contacts, contact_to_update):
    # Initialized input.
    user_input = "yes"
    # For each contact in the contact list, loop.
    for contact in contacts:
        if contact["name"] == contact_to_update:
            while user_input == "yes":
                # While the user has not selected a valid option, loop.
                while user_input != "name" and user_input != "age" and user_input != "email" and user_input != "favorite color":
                    print("Attributes: name, age, email, favorite color")
                    user_input = input("What attribute would you like to update? ").lower()
                # If the user wants to update the name, the program will ask the user for a new name, then save it over the current contact.
                if user_input == "name":
                    user_input = input("What name would you like to set the contact to? ")
                    contact["name"] = user_input
                # If the user wants to update the age, the program will ask the user for a new age, then save it over the current contact.
                elif user_input == "age":
                    while not user_input.isnumeric():
                        user_input = input("What age would you like to set the contact to? ")
                    contact["age"] = user_input
                # If the user wants to update the email, the program will ask the user for a new email, then save it over the current contact.
                elif user_input == "email":
                    user_input = input("What email would you like to set the contact to? ")
                    contact["email"] = user_input
                # If the user wants to update the favorite color, the program will ask the user for a new favorite color, then save it over the current contact.
                elif user_input == "favorite color":
                    user_input = input("What favorite color would you like to set the contact to? ")
                    contact["favorite color"] = user_input
                user_input = str()
                # Checks if the user wants to update another attribute in the contact.
                while user_input != "yes" and user_input != "no":
                    user_input = input("Would you like to update another attribute? (Yes/No) ").lower()
                    if user_input == "no":
                        # Returns the contact list to exit the function
                        return contacts

# Adds a contact to the list of contacts, and returns the list of contacts at the end of the function.
def add_contact(contacts):
    user_input = str()
    # Initialized an empty contact.
    contact = {
        "name": str(),
        "age": int(),
        "email": str(),
        "favorite color": str()
        }
    # Checks to see if the length of the string is 0, cause names typically have at least 1 character in then.
    while len(user_input) == 0:
        user_input = input("What is the contacts name? ")
        contact["name"] = user_input
    # Ages are numeric, and not floats, so if the user does not enter in a while number, it will not work.
    while not user_input.isnumeric():
        user_input = input("What is the contacts age? ")
    contact["age"] = int(user_input)
    # Emails usually have @....com or .net, with a email directory as well, so I decided to make it less than 8 to enter in a valid email.
    while len(user_input) < 8:
        user_input = input("What is the contacts email? ")
        contact["email"] = user_input
        if len(user_input) < 8:
            print("Please enter in a valid email address! (e.g. [name]@email.com")
    user_input = str()
    # I could not find a color with only two characters, so if the user doesn't name a color thats 3 or greater, it will just keep looping.
    while len(user_input) < 3:
        user_input = input("What is the contacts favorite color? ")
        contact["favorite color"] = user_input
    # appends the contact list with the new contact and returns it.
    contacts.append(contact)
    return contacts

# Prints the opening message and a list of options to choose from. 
# Returns the option the user has selected.
# P = print contacts.
# S = specific contact from the list.
# A = adds a contact to the list.
# D = deletes a contact from the list.
# U = updates a contact in the list.
# E = Exits the program and saves the contact list to contacts.json.
def print_opening_message():
    user_input = str()
    print("---------- Contact List Editor ----------")
    print("P = Print Contacts\nS = Print Specific Contact\nA = Add New Contact\nD = Delete Contact\nU = Update Contact\nE = Save and Exit the program")
    while user_input != "p" and user_input != "s" and user_input != "a" and user_input != "d" and user_input != "u" and user_input != "e":
        user_input = input("Please enter in an operation you wish to do: ").lower()
    return user_input

# Loads the contacts
contact_list = load_contacts()
# Initialized inputs
user_input = str()
deleted_user = str()
update_user = str()

# Loops while the user does not want to exit.
while user_input != "e":
    user_input = print_opening_message()
    # Prints the contact list.
    if user_input == "p":
        print_contacts(contact_list)
        input("Press Enter to continue... ")
    # Prints a contact from the list
    elif user_input == "s":
        while True:
            user_input = input("Please enter the name of a contact you wish to see. (enter \"done\" if you do not want to look at anything.) ")
            # Breaks if the user doesn't want to print a specific contact.
            if user_input == "done":
                user_input == "no"
                break
            # Breaks if it can successfully print the contact from the list.
            if print_specific_contact(contact_list, user_input):
                break
        input("Press Enter to continue... ")
    elif user_input == "a":
        contact_list = add_contact(contact_list)
    elif user_input == "d":
        while True:
            deleted_user = input("Please enter the name of a contact you wish to delete. (enter \"done\" if you do not want to look at anything.) ")
            if deleted_user == "done":
                user_input == "no"
                break
            # Breaks if it can successfully print the contact from the list.
            # We use this to verify if the name given is in the contact list since print_specific_contact() returns a boolean.
            if print_specific_contact(contact_list, deleted_user):
                break
        while user_input != "yes" and user_input != "no":
            user_input = input("Are you sure you want to delete this contact? (Yes/No) ").lower()
        # Asks if the user wants to delete the contact or not.
        if user_input == "yes":
            print("deleting contact...")
            contact_list = delete_contact(contact_list, deleted_user)
        elif user_input == "no":
            print("The contact was not deleted.")
        input("Press Enter to continue... ")
    elif user_input == "u":
        while True:
            update_user = input("Please enter the name of a contact you wish to delete. (enter \"done\" if you do not want to look at anything.) ")
            if update_user == "done":
                user_input == "no"
                break
            # Breaks if it can successfully print the contact from the list.
            # We use this to verify if the name given is in the contact list since print_specific_contact() returns a boolean.
            if print_specific_contact(contact_list, update_user):
                break
        # Asks if the user wants to update the contact or not.
        while user_input != "yes" and user_input != "no":
            user_input = input("Are you sure you want to update this contact? (Yes/No) ").lower()
        if user_input == "yes":
            print("updating contact!")
            contact_list = update_contact(contact_list, update_user)
        elif user_input == "no":
            print("The contact was not updated.")
        input("Press Enter to continue... ")

# When the loop exits, it saves the list of contacts to the local .json file.
print("Saving and Exiting!")
save_contacts(contact_list)

        



# print_contacts(contact_list)
# contact_list = delete_contact(contact_list, "Joe")
# print_contacts(contact_list)
# print_specific_contact(contact_list, "Jill")
# contact_list = update_contact(contact_list, "Jane")
# print_contacts(contact_list)
# contact_list = add_contact(contact_list)
# print_contacts(contact_list)