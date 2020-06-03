from django.core.management.base import BaseCommand



class Command(BaseCommand):

    def handle(self, *args, **options):
        with open
        file:
            text = file.read()
        data = json.loads(text)
        for pokemon in data['pokemon']:
            number = pokemon['number']
            name = pokemon['name']
            height = pokemon['height']
            weight = pokemon['weight']
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = pokemon['types']
            varieties = PokemonType(name=types)
            varieties.save()
            
            
            pokemon_types = Pokemon(number=number, name=name, height=height, weight=weight, image_front=image_front, image_back=image_back,)
            
            for poke_type in types:
                if poke_type == types[0]
                    varitiest = PokemonType(name=types)
                    varieties.save()
                elif poke_type == types[1]
                    varities = PokemonType(name=types)
                    varieties.save()
            pokemon_types.save()

            if len(types) == 1:
                

