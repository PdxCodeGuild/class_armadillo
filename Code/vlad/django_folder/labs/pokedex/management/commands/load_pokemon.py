from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json
# from .models import Pokemon


class Command(BaseCommand):
    def handle(self, *args, **options):
        # This is to delete all the rows out of the table each time I run the python3 manage.py load_pokemon it will load a fresh data without dupplicating on the database.
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        # open the file containing the json and  we need to add the relative path with open below: './pokedex/management/commands/pokemon.json'
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            # reading the text in the file
            text = file.read()
            # turning that json string into a python dictionary
            data = json.loads(text)  # bring the variable data to the for loop
            print(data)
            pokemon = data['pokemon']
            # return ''
            print(pokemon)

            # looping over the contact data inside that dictionary
        for pika_data in data['pokemon']:

            # getting out the contact data into local variables
            number = pika_data['number']
            name = pika_data['name']
            height = pika_data['height']
            weight = pika_data['weight']
            image_front = pika_data['image_front']
            image_back = pika_data['image_back']
            types = pika_data['types']

            # create a pokemon from our data
            pokemon = Pokemon(number=number,
                              name=name,
                              height=height,
                              weight=weight,
                              image_front=image_front,
                              image_back=image_back)
            # save the contact to the database
            pokemon.save()

            # loop through each type and associate go through each items and if the type is not there then create it.
            # here we are looping over the dictionary and looking for the data with the key types
            # looping poke_type in the dictionary call pika_data selecting the types ['types']
            for poke_type in pika_data['types']:
                types, created = PokemonType.objects.get_or_create(
                    name=poke_type)
                pokemon.types.add(types)

       # tags - many-to-many =======================================

# Sample of many to many long way and short way:

        # # get a blog post
        # blog_post = BlogPost.objects.get(title='Burrito')
        # # get all the tags associated with a blog post
        # print(blog_post.tags.all())

        # # create a blog post tag
        # # tag = BlogPostTag(name='#delicious')
        # # save it to the database - necessary before we create a relationship with a blog post
        # # tag.save()

        # # check if a record exists, .exists returns true if .filter has any results
        # # if BlogPostTag.objects.filter(name='#delicious').exists():
        # #     tag = BlogPostTag.objects.get(name='#delicious')
        # # else:
        # #     tag = BlogPostTag(name='#delicious')
        # #     tag.save()

        # # get_or_create will get the record if it exists or create it
        # # it returns a tuple, the first value is the record
        # # the second is a boolean that's true if it's created
        # tag, created = BlogPostTag.objects.get_or_create(name='#delicious')

# ===================================================================================

    # number = models.IntegerField()
    # name = models.CharField(max_length=50)
    # height = models.IntegerField()
    # weight = models.IntegerField()
    # image_front = models.CharField(max_length=50)
    # image_back = models.CharField(max_length=50)
    # types = models.ManyToManyField(PokemonType)


# Starter Code by instructor below:
# from django.core.management.base import BaseCommand
# import json
# from contacts.models import Contact

# class Command(BaseCommand):

#     def handle(self, *args, **options):
#         # open the file containing the json
#         with open('./contacts/management/commands/contacts.json', 'r') as file:
#             # reading the text in the file
#             text = file.read()
#         # turning that json string into a python dictionary
#         data = json.loads(text)
#         # looping over the contact data inside that dictionary
#         for contact_data in data['contacts']:
#             # getting out the contact data into local variables
#             first_name   = contact_data['first_name']
#             last_name    = contact_data['last_name']
#             birthday     = contact_data['birthday']
#             email        = contact_data['email']
#             phone_number = contact_data['phone_number']
#             is_cell      = contact_data['is_cell']
#             comments     = contact_data['comments']
#             # create a contact from our data
#             contact = Contact(first_name=first_name,
#                                 last_name=last_name,
#                                 birthday=birthday,
#                                 email=email,
#                                 phone_number=phone_number,
#                                 is_cell=is_cell,
#                                 comments=comments)
#             # save the contact to the database
#             contact.save()
