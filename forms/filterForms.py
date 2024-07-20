import json
f = open('allForms.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

d = dict()


f = open('alltoAPI.json')
allapijson = json.load(f) #list of dictionary of pokemon data
f.close()

allapi=[]
for i in allapijson:
    allapi.append(allapijson[i])

for i in data.keys():
    name = i.split("-")[0]

    if name not in ["iron", "tapu", "nidoran"]:
        if name in d:
            d[name].append(i)
        else:
            d[name] = [i]
    else:
        if i in d:
            d[i].append(i)
        else:
            d[i] = [i]

mult = dict()


for i in d.keys():
    if len(d[i]) > 1:
        mult[i] = []
        if i not in allapi:
            print(i)
        for j in d[i]:
            if (j != i):

                mult[i].append({j:data[j]})

# print(mult)

with open('certainForms.json', 'w') as f:
    json.dump(mult, f)
