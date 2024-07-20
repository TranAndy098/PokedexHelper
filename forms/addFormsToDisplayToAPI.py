import json
f = open('forms2.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()


formedPokemon = list(data.keys())

formDisplay = []
DisplayAPI = []


for i in formedPokemon:
    forms = data[i]
    for j in forms:
        name = list(j.keys())[0]
        disName = j[name]["DisplayName"]
        formDisplay.append([name, disName])
        DisplayAPI.append([disName,i])

f = open('APIToDisplay.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

for i in formDisplay:
    data[i[0]] = i[1]

with open('APIToDisplay2.json', 'w') as f:
    json.dump(data, f)


f = open('displayToAPI.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

for i in DisplayAPI:
    data[i[0]] = i[1]

data2 = data.copy()

for i in data2.keys():
    data[i.lower()] = data[i]

with open('displayToAPI2.json', 'w') as f:
    json.dump(data, f)

