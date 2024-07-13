specialMoves = {"Forest's Curse" :"forests-curse","Double-Edge" :"double-edge","Freeze-Dry" : "freeze-dry","Baby-Doll Eyes" :"baby-doll-eyes","Land's Wrath": "lands-wrath","King's Shield": "kings-shield","Wake-Up Slap": "wake-up-slap","Will-O-Wisp" :"will-o-wisp","V-create": "v-create","U-turn" :"u-turn","Trick-or-Treat" :"trick-or-treat","Topsy-Turvy" :"topsy-turvy","Self-Destruct" :"self-destruct","Power-Up Punch": "power-up-punch", "Nature's Madness": "natures-madness", "Multi-Attack" :"multi-attack", "Lock-On" :"lock-on"}
specialMovesAPI = {'forests-curse': "Forest's Curse", 'double-edge': 'Double-Edge', 'freeze-dry': 'Freeze-Dry', 'baby-doll-eyes': 'Baby-Doll Eyes', 'lands-wrath': "Land's Wrath", 'kings-shield': "King's Shield", 'wake-up-slap': 'Wake-Up Slap', 'will-o-wisp': 'Will-O-Wisp', 'v-create': 'V-create', 'u-turn': 'U-turn', 'trick-or-treat': 'Trick-or-Treat', 'topsy-turvy': 'Topsy-Turvy', 'self-destruct': 'Self-Destruct', 'power-up-punch': 'Power-Up Punch', 'natures-madness': "Nature's Madness", 'multi-attack': 'Multi-Attack', 'lock-on': 'Lock-On'}


import requests
import json


def correctName(apiName):
    components = apiName.split("-")
    for i in range(len(components)):
        components[i] = components[i].capitalize()
    return " ".join(components)


apim= dict()


for i in range(1, 920):
    print(i)
    cur = dict()
    urlL = f"https://pokeapi.co/api/v2/move/{i}"
    response = requests.get(urlL)
    response = response.json()

    apiName = response["name"]
    cur["APIName"] = apiName

    realName = ""
    if apiName in specialMovesAPI:
        realName = specialMovesAPI[apiName]
    else:
        realName = correctName(apiName)
    cur["realName"] = realName

    accuracy = response["accuracy"]
    cur["Accuracy"] = accuracy if accuracy != None else "---"

    effect_chance = response["effect_chance"]
    cur["Effect Chance"] = effect_chance if effect_chance != None else "---"

    damage_class = response["damage_class"]["name"]
    cur["Damage Class"] = damage_class

    effects = ""

    if (len(response["effect_entries"]) > 0):
        effects = response["effect_entries"][0]["short_effect"]
    cur["Effects"] = effects

    power = response["power"]
    cur["Power"] = power if power != None else "---"

    pp = response["pp"]
    cur["PP"] = pp

    target = response["target"]["name"]
    cur["Target"] = target

    typing = response["type"]["name"]
    cur["Type"] = typing

    cur["URL"] = urlL








    apim[apiName]=cur


with open('allAPIMoves.json', 'w') as f:
    json.dump(apim, f)


