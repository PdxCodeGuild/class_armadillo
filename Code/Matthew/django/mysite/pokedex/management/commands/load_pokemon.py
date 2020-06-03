
from django.core.management.base import BaseCommand

import requests

# from .models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **options):

        response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_armadillo/master/4%20Django/labs/pokemon.json')
        print(response.text)

        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
            print(text)
