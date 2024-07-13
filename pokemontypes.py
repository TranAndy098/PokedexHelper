
import requests
import json


pktypes = dict()

alltypes = []

distoapi = dict()
apitodis = dict()

for i in range(1,19):
    print(i)
    
    urlL = f"https://pokeapi.co/api/v2/type/{i}"
    response = requests.get(urlL)
    response = response.json()

    d = dict()

    spacilTypeto = []
    spacilTypefrom = []

    double_damage_from = response["damage_relations"]["double_damage_from"]
    twodamagefrom = []
    for i in double_damage_from:
        twodamagefrom.append(i["name"])
        spacilTypefrom.append(i["name"])

    double_damage_to = response["damage_relations"]["double_damage_to"]
    twodamageto = []
    for i in double_damage_to:
        twodamageto.append(i["name"])
        spacilTypeto.append(i["name"])

    half_damage_from = response["damage_relations"]["half_damage_from"]
    halfdamagefrom = []
    for i in half_damage_from:
        halfdamagefrom.append(i["name"])
        spacilTypefrom.append(i["name"])

    half_damage_to = response["damage_relations"]["half_damage_to"]
    halfdamageto = []
    for i in half_damage_to:
        halfdamageto.append(i["name"])
        spacilTypeto.append(i["name"])

    no_damage_from = response["damage_relations"]["no_damage_from"]
    nodamagefrom = []
    for i in no_damage_from:
        nodamagefrom.append(i["name"])
        spacilTypefrom.append(i["name"])

    no_damage_to = response["damage_relations"]["no_damage_to"]
    nodamageto = []
    for i in no_damage_to:
        nodamageto.append(i["name"])
        spacilTypeto.append(i["name"])
    
    normalTo = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
    for i in spacilTypeto:
        if i in normalTo:
            normalTo.remove(i)

    normalFrom = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
    for i in spacilTypefrom:
        if i in normalFrom:
            normalFrom.remove(i)
    

    id = response["id"]
    name = response["name"]
    realName = name.capitalize()

    alltypes.append(realName)
    distoapi[realName] = name
    apitodis[name] = realName

    move = response["moves"]
    moves = []
    for i in move:
        moves.append(i["name"])

    pokemon = response["pokemon"]
    pokemons = []
    for i in pokemon:
        pokemons.append(i["pokemon"]["name"])


    d["Name"] = name
    d["RealName"] = realName
    d["ID"] = id
    d["URL"] = urlL

    d["NormalTo"] = normalTo
    d["StrongTo"] = twodamageto
    d["WeakTo"] = halfdamageto
    d["ImmuneTo"] = nodamageto

    d["NormalFrom"] = normalFrom
    d["StrongFrom"] = twodamagefrom
    d["WeakFrom"] = halfdamagefrom
    d["ImmuneFrom"] = nodamagefrom
    

    d["Pokemon"] = pokemons
    d["Moves"] = moves

    pktypes[name] = d.copy()


alltypes.sort()


with open('allTypeData.json', 'w') as f:
    json.dump(pktypes, f)

with open('allTypes.json', 'w') as f:
    json.dump(alltypes, f)

with open('typeAPIToDisplay.json', 'w') as f:
    json.dump(apitodis, f)

with open('typeDisplayToAPI.json', 'w') as f:
    json.dump(distoapi, f)

