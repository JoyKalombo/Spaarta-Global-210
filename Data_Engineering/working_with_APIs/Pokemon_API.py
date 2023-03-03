import requests
import random
import json

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/krokorok")

print(pokemon_req.status_code)

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118")
data = response.json()

random_pokemon = random.choice(data["results"])

response = requests.get(random_pokemon["url"])
data = response.json()
name = data['name']
print(name)

# We need to create a game
# 1 player mode (user gets a pokemon (random or not) and that pokemon fights a random pokemon selected by my program)
# 2 player mode (both users get a pokemon (random or not) and they fight to see who the winner is)
#
# Tomorrow, we are creating azure functions and our own APIs