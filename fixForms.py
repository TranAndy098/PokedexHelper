import json
f = open('displayToAPI.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

names = list(data.values())

f = open('certainForms2.json')
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


    newDict[newName] = data[mon]


with open('forms2.json', 'w') as f:
    json.dump(newDict, f)
