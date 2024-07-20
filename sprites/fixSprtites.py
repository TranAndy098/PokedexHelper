import json
f = open('certainForms.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('allSprites.json')
data2 = json.load(f) #list of dictionary of pokemon data
f.close()

nd = dict()


for i in data2.keys():
    nd[i] = data2[i]
    smaller = i.split("-")[0]
    if (smaller in data):
        i = smaller
        for j in range(len(data[i])):
            for k in data[i][j]:
                n = data[i][j][k]["Name"]
                nd[n] = {"Name": n, "FrontDefault": data[i][j][k]["FrontDefault"], "BackDefault": data[i][j][k]["BackDefault"], "FrontShiny": data[i][j][k]["FrontShiny"], "BackShiny": data[i][j][k]["BackShiny"]}
    elif (i == "mr. mime") or (i in data):
        for j in range(len(data[i])):
            for k in data[i][j]:
                n = data[i][j][k]["Name"]
                nd[n] = {"Name": n, "FrontDefault": data[i][j][k]["FrontDefault"], "BackDefault": data[i][j][k]["BackDefault"], "FrontShiny": data[i][j][k]["FrontShiny"], "BackShiny": data[i][j][k]["BackShiny"]}
        


with open('allSprites.json', 'w') as f:
    json.dump(nd, f)