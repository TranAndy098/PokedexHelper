import json
f = open('data.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

import requests
curPokemon = "venusaur"

b_line = ["bulbasaur", "ivysaur", "venusaur"]

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{curPokemon.lower()}")

response = response.json()


print("Sprites")
print(response["sprites"]["front_default"])
print(response["sprites"]["back_default"])
print(response["sprites"]["front_shiny"])
print(response["sprites"]["back_shiny"])
print("--------------------------------------------------------------------")

print("types")
for i in response["types"]:
    print(i["type"]["name"])
print("--------------------------------------------------------------------")


print("abilities")
for i in response["abilities"]:
    print(i["ability"]["name"], i["is_hidden"])
print("--------------------------------------------------------------------")


print("stats")
for i in response["stats"]:
    print(i["stat"]["name"], i["base_stat"])
print("--------------------------------------------------------------------")


print("moves")
for i in response["moves"]:
    print("--------------------------------------------------------------------")
    print(i["move"]["name"])
    move_url = i["move"]["url"]
    response = requests.get(move_url)
    response = response.json()
    print("accurancy", response["accuracy"], type(response["accuracy"]))
    print("effect_chance", response["effect_chance"], type(response["effect_chance"]))
    print("damage_class", response["damage_class"]["name"], type(response["damage_class"]["name"]))
    if (len(response["effect_entries"]) > 0):
        print("effects", response["effect_entries"][0]["short_effect"], type(response["effect_entries"][0]["short_effect"]))
    print("power", response["power"], type(response["power"]))
    print("pp", response["pp"], type(response["pp"]))
    print("target", response["target"]["name"], type(response["target"]["name"]))
    print("type", response["type"]["name"], type(response["type"]["name"]))

print("--------------------------------------------------------------------")


