
import requests
import json

response = requests.get("https://pokeapi.co/api/v2/version-group/?limit=75")
response = response.json()

# list of all locaitons with api name an durl 
allEncounters = response["results"]

disAPI = dict()
APIdis = dict()

num = 1

def correctName(apiName):
    components = apiName.split("-")
    for i in range(len(components)):
        components[i] = components[i].capitalize()
    return " ".join(components)

# for all regular locaiton-area
for i in allEncounters:
    print(num, "/", 71)
    name, urL = list(i.keys())
    name = i[name]
    urL = i[urL]

    response = requests.get(urL)
    response = response.json()

    for v in response["versions"]:
        vname, vurL = list(i.keys())
        vname = v[vname]
        vurL = v[vurL]

        Display = correctName(vname)

        response = requests.get(vurL)
        response = response.json()

        disNames = response["names"]

        for lang in disNames:
            if lang["language"]["name"] == "en":
                Display = lang["name"]
        
        disAPI[Display] = vname
        APIdis[vname] = Display
    
    num += 1


with open('gamesDisplayToAPI.json', 'w') as f:
    json.dump(disAPI, f)

with open('gamesAPIToDisplay.json', 'w') as f:
    json.dump(APIdis, f)


# for all palpark locaitons

