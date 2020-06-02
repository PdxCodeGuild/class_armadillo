from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./db.json', 'r') as file:
            data = json.loads(file.read())
            pokemon = data['pokemon']
        stored_pokemon = Pokemon.objects.get()
        for i in pokemon:

        return print(pokemon)