import json

f = open('data.json')


data = json.load(f)

d = dict()

for i in data:
    cur = dict()




    cur["Name"] = i["name"]
    cur["ID"] = i["id"]
    cur["Evolve_ID"] = i["evolve_id"]
    cur["EvolveChain"] = i["evolve_chain"]

    cur["EvolveFrom"] = i["evolve_from"]
    cur["EvolveInto"] = i["evolve_into"]
    cur["Size"] = len(i["evolve_chain"])
    
    d[i["name"].lower()] = cur

f.close()

with open('evolutionChains.json', 'w') as f:
    json.dump(d, f)


