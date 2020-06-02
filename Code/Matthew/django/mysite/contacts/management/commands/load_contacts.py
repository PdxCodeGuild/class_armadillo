from django.core.management.base import BaseCommand
import json
from contacts.models import Contact

class Command(BaseCommand):

    def handle(self, *args, **options):
        # open the file containing the json
        with open('./contacts/management/commands/contacts.json', 'r') as file:
            # reading the text in the file
            text = file.read()
        # turning that json string into a python dictionary
        data = json.loads(text)
        # looping over the contact data inside that dictionary
        for contact_data in data['contacts']:
            # getting out the contact data into local variables
            first_name   = contact_data['first_name']
            last_name    = contact_data['last_name']
            birthday     = contact_data['birthday']
            email        = contact_data['email']
            phone_number = contact_data['phone_number']
            is_cell      = contact_data['is_cell']
            comments     = contact_data['comments']
            # create a contact from our data
            contact = Contact(first_name=first_name,
                                last_name=last_name,
                                birthday=birthday,
                                email=email,
                                phone_number=phone_number,
                                is_cell=is_cell,
                                comments=comments)
            # save the contact to the database
            contact.save()


        