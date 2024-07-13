import json
f = open('data.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

import requests
curPokemon = "venusaur"

b_line = ["bulbasaur", "ivysaur", "venusaur"]

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{curPokemon.lower()}/encounters")

response = response.json()




for entry in response:
    where = entry["location_area"]["name"]
    method = entry["version_details"][0]["encounter_details"][0]["method"]["name"]
    game = entry["version_details"][0]["version"]["name"]
    print(game, where, method)
    print("--------------------------")
