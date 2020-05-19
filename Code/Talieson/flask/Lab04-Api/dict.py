pokedex = {
    "pokemon": [
        {
            "id": 16,
            "name": "Pidgey"
        },
        {
            "id": 513,
            "name": "Pansear"
        },
        {
            "id": 150,
            "name": "Mewtwo"
        },
        {
            "id": 291,
            "name": "Ninjask"
        }
    ]
}

pokedex = sorted(pokedex["pokemon"], key = lambda i: i["id"])

print(pokedex)