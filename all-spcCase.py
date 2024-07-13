
filea = open('all.txt', 'r')
Lines = filea.readlines()

ap = []

for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])

    ap.append(b.lower())

filea.close()


print(ap)

import requests
import json

apim= dict()


for i in range(1, 1026):
    print(i)
    cur = dict()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    response = response.json()

    name = response["name"]
    spritesFront = response["sprites"]["front_default"]
    spritesBack = response["sprites"]["back_default"]
    spritesFrontShiny = response["sprites"]["front_shiny"]
    spritesBackShiny = response["sprites"]["back_shiny"]

    cur["Name"] = name
    cur["FrontDefault"] = spritesFront
    cur["BackDefault"] = spritesBack
    cur["FrontShiny"] = spritesFrontShiny
    cur["BackShiny"] = spritesBackShiny


    apim[name]=cur


import json

with open('allSPCCase.json', 'w') as f:
    json.dump(ap, f)



    
