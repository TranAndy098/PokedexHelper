import requests
import json


response = requests.get("https://pokeapi.co/api/v2/move-target/")

abilities = response.json()["results"]

def display(name):
    pieces = name.split("-")
    for i in range(len(pieces)):
        pieces[i] = pieces[i].capitalize()
    return " ".join(pieces)

disAPI = dict()
APIdis = dict()
abbilitesData = dict()


for i in abilities:
    name = i["name"]
    URa = i["url"]
    disName = display(name)

    c = dict()

    disAPI[disName] = name
    APIdis[name] = disName

    c["Name"] = name
    c["DisplayName"] = disName
    c["URL"] = URa

    abbilitesData[name] = c
    


with open('allMoveTargetData.json', 'w') as f:
    json.dump(abbilitesData, f)


with open('moveTargetAPIToDisplay.json', 'w') as f:
    json.dump(APIdis, f)

with open('moveTargetDisplayToAPI.json', 'w') as f:
    json.dump(disAPI, f)