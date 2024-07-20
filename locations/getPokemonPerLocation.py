import json

f = open('pokemonGameLocations.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('locationNamesAPIToDisplay.json')
locations2 = json.load(f) #list of dictionary of pokemon data
f.close()


loc_Encounters = dict()

for l in locations2:
    loc_Encounters[l] = dict()



pokemon = list(data.keys())


# for all regular locaiton-area
for i in pokemon:
    games = list(data[i].keys())
    for game in games:
        locations = list(data[i][game].keys())
        for location in locations:
            loc_Encounters[location][i] = data[i][game][location]


with open('pokemonPerLocation.json', 'w') as f:
    json.dump(loc_Encounters, f)
