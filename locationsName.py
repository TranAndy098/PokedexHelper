
import requests
import json

response = requests.get("https://pokeapi.co/api/v2/location-area/?limit=1054")
response = response.json()

# list of all locaitons with api name an durl 
allPlaces = response["results"]

disAPI = dict()
APIdis = dict()

def correctName(apiName):
    components = apiName.split("-")
    for i in range(len(components)):
        components[i] = components[i].capitalize()
    return " ".join(components)

num = 1

# for all regular locaiton-area
for i in allPlaces:
    print(num, "/", 1054)
    name, urL = list(i.keys())
    name = i[name]
    urL = i[urL]


    response = requests.get(urL)
    response = response.json()


    Display = correctName(name)

    disNames = response["names"]

    for lang in disNames:
        if lang["language"]["name"] == "en":
            Display = lang["name"]
    
    disAPI[Display] = name
    APIdis[name] = Display


    num += 1


with open('locationNamesAPIToDisplay.json', 'w') as f:
    json.dump(APIdis, f)

with open('locationNamesDisplayToAPI.json', 'w') as f:
    json.dump(disAPI, f)


# for all palpark locaitons

