from django.core.management.base import BaseCommand

from pokedex.models import Pokemon, Type
import json

def add_pokemon(pokemon):
    all_types = Type.objects.all()
    new_type = ''
    new_pokemon = Pokemon(number=pokemon['number'], name=pokemon['name'], height=pokemon['height'], weight=pokemon['weight'], image_front=pokemon['image_front'], image_back=pokemon['image_back'])
    new_pokemon.save()
    for i in range(len(pokemon['types'])):
        if not Type.objects.filter(name=pokemon['types'][i]):
            print(pokemon['types'][i])
            new_type = Type(name=pokemon['types'][i])
            new_type.save()
        else:
            new_type = Type.objects.get(name=pokemon['types'][i])
        new_pokemon.types.add(new_type)
    print(all_types)
    print(new_pokemon)

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        print(data['pokemon'])
        for i in range(len(data['pokemon'])):
            add_pokemon(data['pokemon'][i])
