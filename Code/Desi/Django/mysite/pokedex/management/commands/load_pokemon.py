from django.core.management.base import BaseCommand



class Command(BaseCommand):

    def handle(self, *args, **options):
        # open the file containing json
        with open('./contacts/management/commands/contacts.json', 'r') as file:
            # reading the text in the file
        file:
            #reading the text in the file
            text = file.read()
        # turning json string into a python dictionary
        data = json.loads(text)
        # looping over the contact data inside the dictionary
        for pokemon in data['pokemon']:
            # getting out the contact data into local variables
            number = pokemon['number']
            name = pokemon['name']
            height = pokemon['height']
            weight = pokemon['weight']
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = pokemon['types']
            varieties = PokemonType(name=types)
            varieties.save()
            
            # create a contact from out data
            pokemon_types = Pokemon(number=number, name=name, height=height, weight=weight, image_front=image_front, image_back=image_back,)
            
            # save contact to the database

            contact.save()

