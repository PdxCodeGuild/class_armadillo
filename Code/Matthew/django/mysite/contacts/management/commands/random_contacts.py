from django.core.management.base import BaseCommand
import random
from contacts.models import Contact
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        first_names = ['Jane', 'Joe', 'John', 'Jimmy', 'Job', 'Mark']
        last_names = ['Jones', 'Frasier', 'Kringleberry', 'Marsh', 'Bellingham']
        for i in range(300):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            birthday = datetime.datetime.now() - datetime.timedelta(days=random.randint(1000,10000))
            contact = Contact(first_name=first_name,
                                last_name=last_name,
                                birthday=birthday,
                                email='person@gamil.com',
                                is_cell=random.choice([True, False]),
                                comments='blah blah blah')
            contact.save()
