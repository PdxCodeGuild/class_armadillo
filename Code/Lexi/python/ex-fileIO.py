# # Create a contact: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.

f = open('filename.txt')  # open the file
contents = f.read()  # read the contents
print(contents)
# Retrieve a contact: ask the user for the contact's name, find the user with the given name, and display their information

import os
folder_path = '...'
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            print(f.read())
# Update a contact: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a contact: ask the user for the contact's name, remove the contact with the given name from the contact list.
# List a contact: list all the contacts and their information
# Exit: save the contacts to a file and exit the program

f.close()  # close the file

path = 'test1.txt'
with open(path, 'r') as file:
    lines = file.read().split('\n')
    for line in file:
        print(line)