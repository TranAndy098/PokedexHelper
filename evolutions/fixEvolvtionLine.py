import json
f = open('displayToAPI.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

names = list(data.values())

f = open('evolutionChains.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

newDict = dict()

mons_old = list(data.keys())

difference = []

for i in names:
    if i not in mons_old:
        difference.append(i)

forms = dict()

for i in difference:
    shorter = i.split("-")[0]
    forms[shorter] = i



for i in range(len(mons_old)):
    mon = mons_old[i]
    newName = mon
    if mon in forms:
        newName = forms[mon]
    
    for i in data[mon]["EvolveChain"]:
        for j in range(len(i)):
            if i[j] in forms:
                i[j] = forms[i[j]]

    if (len(data[mon]["EvolveFrom"]) > 0 ) and (data[mon]["EvolveFrom"][0] in forms):
        data[mon]["EvolveFrom"][0] = forms[data[mon]["EvolveFrom"][0]]


    for i in range(len(data[mon]["EvolveInto"])):
        if data[mon]["EvolveInto"][i] in forms:
            data[mon]["EvolveInto"][i] = forms[data[mon]["EvolveInto"][i]]


    data[mon]["Name"] = newName
    newDict[newName] = data[mon]


with open('evolutionLines2.json', 'w') as f:
    json.dump(newDict, f)
