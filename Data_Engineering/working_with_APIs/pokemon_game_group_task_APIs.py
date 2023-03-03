import requests
import random
import json

all_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118").json()


def get_pokemon():
    random_pokemon = random.choice(all_pokemon["results"])
    return random_pokemon


def retrieve_base_experience(pokemon):
    response = requests.get(pokemon["url"]).json()
    base_experience = response["base_experience"]
    return base_experience


player1_pokemon = get_pokemon()
print(player1_pokemon["name"])
base_experience1 = retrieve_base_experience(player1_pokemon)
print(base_experience1)

print(" ")

player2_pokemon = get_pokemon()
print(player2_pokemon["name"])
base_experience2 = retrieve_base_experience(player2_pokemon)
print(base_experience2)

print(" ")

if base_experience1 > base_experience2 and (base_experience1 is not None) and (base_experience2 is not None):
    print(player1_pokemon["name"], "wins because", player1_pokemon["name"] + "'s base experience is",
          (base_experience1 - base_experience2), "more than that of", player2_pokemon["name"])
elif base_experience1 < base_experience2:
    print(player2_pokemon["name"], "wins because", player2_pokemon["name"] + "'s base experience is",
          (base_experience2 - base_experience1), "more than that of", player1_pokemon["name"])
else:
    print("we have a draw!!!")

# How to deal with when base experience returns "none"
