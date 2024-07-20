
import requests
import json


disAPI = dict()

for i in range(1,10):
    disAPI[i] = []



# for all regular locaiton-area
for i in range(1,10):
    print(i, "/", 9)
    

    response = requests.get(f"https://pokeapi.co/api/v2/generation/{i}")
    response = response.json()

    ver_groups = response["version_groups"]

    for v in ver_groups:
        vname, vurL = list(v.keys())
        vname = v[vname]
        vurL = v[vurL]

        response = requests.get(vurL)
        response = response.json()

        versions = response["versions"]

        for ver in versions:
            name, urL = list(ver.keys())
            name = ver[name]
            urL = ver[urL]
            disAPI[i].append(name)



with open('gamesPerGen.json', 'w') as f:
    json.dump(disAPI, f)




