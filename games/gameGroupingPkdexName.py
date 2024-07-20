
import requests
import json

def correctName(apiName):
    components = apiName.split("-")
    for i in range(len(components)):
        components[i] = components[i].capitalize()
    return " ".join(components)

pokedex_names = dict()

response = requests.get(f"https://pokeapi.co/api/v2/pokedex/?limit=100")
response = response.json()

results=response["results"]

disAPI = dict()
APIdis = dict()



num = 1
for i in results:
    print(num, "/", 33)
    if num != 10:

        vname, vurL = list(i.keys())
        vname = i[vname]
        vurL = i[vurL]

        disP = correctName(vname)

        disAPI[disP] = vname
        APIdis[vname] = disP



            
                
    num += 1
                




with open('pokedexDisplayToAPI.json', 'w') as f:
    json.dump(disAPI, f)

with open('pokedexAPIToDisplay.json', 'w') as f:
    json.dump(APIdis, f)


