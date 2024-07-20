

import requests

import json
"""
id_evolve = dict()

pk_id = dict()

for num in range(1, 550):
    print(num)
    response = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{num}")
    try:
        l = []
        a = response.json()["chain"]["species"]["name"]

        b = response.json()["chain"]["evolves_to"]
    

        if len(b) == 0:
            l.append([a])
        else:
            for i in b:
                c = i["species"]["name"]
                d = i["evolves_to"]


                if len(d) == 0:
                    l.append([a,c])
                else:
                            
                    for j in d:
                        e = j["species"]["name"]
                        l.append([a,c,e])          
                            

        id_evolve[num] = l

        for i in l:
            for j in i:
                pk_id[j] = num
    except:
        print(num,"--------------------------------------------------------")

#print(id_evolve) #id to [pokemons]

#print(pk_id) #pokmeon to id
with open('evolveIDToPokemon.json', 'w') as f:
    json.dump(id_evolve, f)
with open('PokemonToEvolveId.json', 'w') as f:
    json.dump(pk_id, f)
"""
f = open('evolveIDToPokemon.json')
id_evolve = json.load(f) #list of dictionary of pokemon data
f.close()



f = open('PokemonToEvolveId.json')
pk_id = json.load(f) #list of dictionary of pokemon data
f.close()



print(2)
lp = dict()
i = 1
for p in list(pk_id.keys()):
    print(i)
    try:
        c_d = dict()
        name = p
        print(21)
        id = i
        evolve_id = pk_id[name]
        print(22)
        evolve_chain = id_evolve[str(evolve_id)]
        print(23)
        c_d["Name"] = name
        c_d["ID"] = id
        c_d["Evolve_ID"] = evolve_id
        c_d["EvolveChain"] = evolve_chain
        print(24)
        evolve_from = []
        evolve_into = []
        print(25)
        for c in evolve_chain:
            for i in range(len(c)):
                if c[i] == name:
                    if i > 0:
                        evolve_from.append(c[i-1])
                    if i < len(c) - 1:
                        evolve_into.append(c[i+1])
        print(26)
        c_d["EvolveFrom"] = evolve_from
        c_d["EvolveInto"] = evolve_into
        c_d["Size"] = len(evolve_chain)
        print(27)
        lp[name] = c_d.copy()
    except:
        print(p)
    i += 1

print(3)


with open('evolutionChains.json', 'w') as f:
    json.dump(lp, f)



