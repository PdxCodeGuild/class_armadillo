

# Lab 4: Pokedex

Let's build a searchable pokedex!

## Part 1

Create an app for our `pokedex` and add two models to store our pokemon, `Pokemon` and `PokemonType`.

`PokemonType` should have the following fields:
- `name` (CharField)

`Pokemon` should have the following fields:
- `number` (IntegerField)
- `name` (CharField)
- `height` (IntegerField)
- `weight` (IntegerField)
- `image_front` (CharField)
- `image_back` (CharField)
- `types` (MantToManyField with `PokemonType`)


Write a [custom management command](../docs/01%20-%20Django%20Overview.md#custom-management-commands) to load the data from [pokemon.json](./pokemon.json) into your database. To handle the types, check out [many to many fields](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/).

## Part 2

Write a `view`, `route` and `template` to show a list of pokemon on the front page. You can either show all the information as a table, or show only their name and icon and link to a detail page with all their information. Use `<img src="...">` to display their front and back image.

## Part 3

Add a form at the top of your list of pokemon with a text input to search for pokemon. Only show pokemon that match that text input ([search](https://docs.djangoproject.com/en/3.0/topics/db/search/), [icontains](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#std:fieldlookup-icontains)).

## Part 4 (optional)

Use the django [paginator](https://docs.djangoproject.com/en/3.0/topics/pagination/) to only show 20 pokemon at a time, allow the user to switch between pages. [example](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html).

