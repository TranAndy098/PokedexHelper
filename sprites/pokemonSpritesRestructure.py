import json


f = open('allPokemonSprites.json')
data2 = json.load(f) #list of dictionary of pokemon data
f.close()

pokemon = list(data2.keys())

mainname = dict()
notbothsprites= dict()
notshinysprites= dict()
notregsprites= dict()
firstname = dict()

for mon in pokemon:
    entry = data2[mon]["EntryMainName"]
    if entry not in pokemon:
        mainname[mon]= entry
        if entry not in firstname:
            firstname[entry] = []
        firstname[entry].append(mon)
    fd = data2[mon]["FrontDefault"]
    fs = data2[mon]["FrontShiny"]

    if fd == None and fs == None:
        notbothsprites[mon] = mon
        notshinysprites[mon] = mon
        notregsprites[mon] = mon
    elif fs == None:
        notshinysprites[mon] = mon
    elif fd == None:
        notshinysprites[mon] = mon

dif = dict()

for k in list(notshinysprites.keys()):
    if k not in notregsprites:
        dif[k]=k


for mon in pokemon:
    entry = data2[mon]["EntryMainName"]
    if entry in firstname:
        data2[mon]["EntryMainName"] = firstname[entry][0]


with open('mainSpriteDoesntExist.json', 'w') as f:
    json.dump(mainname, f)

with open('SpriteDoesnthaveboth.json', 'w') as f:
    json.dump(notbothsprites, f)

with open('Spritenoshiny.json', 'w') as f:
    json.dump(notshinysprites, f)

with open('Spritenoreg.json', 'w') as f:
    json.dump(notregsprites, f)

with open('Spriteregbutnoshiny.json', 'w') as f:
    json.dump(dif, f)

with open('allPokemonSprites.json', 'w') as f:
    json.dump(data2, f)
