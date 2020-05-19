import json
from flask import Flask, render_template, redirect, request, jsonify
from flask_restful import Resource, Api
import random
import requests

app = Flask(__name__)

@app.route('/')
def index():
    pokedex = load_pokedex()
    return render_template("index.html", pokedex=pokedex["pokemon"])


@app.route(f'/generate', methods=["POST"])
def pokemon():
    random_pokemon = random.randint(1, 890)
    new_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}")
    new_pokemon = json.loads(new_pokemon.text)
    
    pokedex = load_pokedex()
    for number in pokedex["pokemon"]:
        if new_pokemon["id"] == number["id"]:
            # result = f"You've already encounted that Pokemon!!"
            return redirect('/')

    pokedex["pokemon"].append({"id":new_pokemon["id"], "name":new_pokemon["forms"][0]["name"].capitalize()})
    save_pokedex(pokedex)
    return redirect('/')


# opens db.json, turns the python dictionary into json, and saves it to the file
def load_pokedex():
     with open('pokedex.json', 'r') as file:
         data = json.loads(file.read())
     return data


# opens db.json, turns the python dictionary into json, and saves it to the file
def save_pokedex(data):
    with open('pokedex.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)