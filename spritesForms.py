import json
f = open('certainForms.json')
forms = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('allSprites.json')
sprites = json.load(f) #list of dictionary of pokemon data
f.close()

formsToReg = dict()


for i in forms:
    mon = i
    for j in forms[i]:
        speForm = list(j.keys())[0]
        formsToReg[speForm] = mon

spritesNew = dict()

for i in sprites.keys():
    new = dict()
    new["Name"] = sprites[i]["Name"]
    if i in formsToReg:
        new["EntryMainName"] = formsToReg[i]
    else:
        new["EntryMainName"] = i

    
    new["FrontDefault"] = sprites[i]["FrontDefault"]
    new["BackDefault"] = sprites[i]["BackDefault"]
    new["FrontShiny"] = sprites[i]["FrontShiny"]
    new["BackShiny"] = sprites[i]["BackShiny"]

    spritesNew[i] = new

with open('allSpriteData.json', 'w') as f:
    json.dump(spritesNew, f)
