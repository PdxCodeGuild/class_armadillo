from django.core.management.base import BaseCommand
import json

# from .models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('pokemon.json', 'r') as file: # open file
            pokemon = json.loads(file.read()) # read the file and convert json to dictionary
        # pokemon = pokemon['pokemon'] # extract the list inside dict
        return pokemon