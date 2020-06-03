from django.core.management.base import BaseCommand
import json
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./pokeapp/management/commands/pokemon.json', 'r') as file: # open the file
            text = file.read() # read the text
            context = json.loads(text) # convert the text containing json into a dictionary
            pokemon = context['pokemon'] # extract the list inside the dictionary