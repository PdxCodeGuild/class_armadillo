from django.core.management.base import BaseCommand
import json
import requests
from contacts.models import Contact
from contacts import secrets

# https://developers.google.com/maps/documentation/geocoding/start

class Command(BaseCommand):
    def handle(self, *args, **options):
        for contact in Contact.objects.all():
            # if either the contact's lat or lng are not zero skip over them
            # if contact.latitude != 0 or contact.longitude != 0:
            #     continue
            url = f'https://maps.googleapis.com/maps/api/geocode/json'
            response = requests.get(url, params={
                'address': contact.location,
                'key': secrets.google_api_key
            })
            data = response.json()
            location = data['results'][0]['geometry']['location']
            # print(response.json())
            # return
            # print(location)
            contact.latitude = location['lat']
            contact.longitude = location['lng']
            contact.save()

