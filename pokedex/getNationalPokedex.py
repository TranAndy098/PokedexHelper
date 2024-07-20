import json


f = open('APIToDisplay2.json')
data2 = json.load(f) #list of dictionary of pokemon data
f.close()

national = dict()
pokemon = list(data2.keys())

br = False

for mon in pokemon:
    if (mon == "venusaur-mega"):
        break

    national[mon] = data2[mon]


with open('nationalPokedexNames.json', 'w') as f:
    json.dump(national, f)
