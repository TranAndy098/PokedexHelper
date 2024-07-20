

import requests
import json

apim= dict()

results = requests.get("https://pokeapi.co/api/v2/pokemon-form/?limit=1473")
results = results.json()["results"]


for i in range(len(results)):
    print(i)
    cur = dict()
    response = requests.get(results[i]["url"])
    response = response.json()

    name = response["name"]
    cur["Name"] = name

    form_name = response["form_name"]
    cur["FormName"] = form_name

    form_order = response["form_order"]
    cur["FormOrder"] = form_order

    id = response["id"]
    cur["ID"] = id

    is_battle_only = response["is_battle_only"]
    cur["isBattleOnly"] = is_battle_only

    is_default = response["is_default"]
    cur["isDefault"] = is_default

    is_mega = response["is_mega"]
    cur["isMega"] = is_mega

    order = response["order"]
    cur["Order"] = order

    pokemon = response["pokemon"]
    cur["Pokemon"] = pokemon


    spritesFront = response["sprites"]["front_default"]
    cur["FrontDefault"] = spritesFront
    spritesBack = response["sprites"]["back_default"]
    cur["BackDefault"] = spritesBack
    
    spritesFrontShiny = response["sprites"]["front_shiny"]
    cur["FrontShiny"] = spritesFrontShiny
    spritesBackShiny = response["sprites"]["back_shiny"]
    cur["BackShiny"] = spritesBackShiny

    typing = response["types"]
    cur["Types"] = typing

    apim[name]=cur


import json

with open('allForms.json', 'w') as f:
    json.dump(apim, f)



    
