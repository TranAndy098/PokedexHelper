sp_ca = {

    "farfetchd":"farfetch'd",
"mr-mime": "mr. mime",
"mime-Jr"  :"mime Jr." ,
"Type-Null":"Type: Null",
"Tapu-Koko" :"Tapu Koko",
"Tapu-Lele" :"Tapu Lele",
"Tapu-Bulu":"Tapu Bulu",
"Tapu-Fini":"Tapu Fini",
"Sirfetchd":"Sirfetch'd",
"Mr-Rime":"Mr. Rime",
"Great-Tusk":"Great Tusk",
"Scream-Tail":"Scream Tail",
"Brute-Bonnet":"Brute Bonnet",
"Flutter-Mane":"Flutter Mane",
"Slither-Wing":"Slither Wing",
"Sandy-Shocks":"Sandy Shocks",
"Iron-Treads":"Iron Treads",
"Iron-Bundle":"Iron Bundle",
"Iron-Hands":"Iron Hands",
"Iron-Jugulis":"Iron Jugulis",
"Iron-Moth":"Iron Moth",
"Iron-Thorns":"Iron Thorns",
"Roaring-Moon":"Roaring Moon",
"Iron-Valiant":"Iron Valiant",
"Walking-Wake":"Walking Wake",
"Iron-Leaves":"Iron Leaves",
"Gouging-Fire":"Gouging Fire",
"Raging-Bolt":"Raging Bolt",
"Iron-Boulder":"Iron Boulder",
"Iron-Crown":"Iron Crown"
}



import requests

for i in sp_ca.copy():
    sp_ca[i.lower()] = sp_ca[i].lower()

print(sp_ca)

print(0)



id_evolve = dict()

pk_id = dict()

for num in range(1, 550):
    response = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{num}")
    try:
        l = []
        a = response.json()["chain"]["species"]["name"]

        if a in sp_ca:
            a = sp_ca[a]

        b = response.json()["chain"]["evolves_to"]
    

        if len(b) == 0:
            l.append([a])
        else:
            for i in b:
                c = i["species"]["name"]
                d = i["evolves_to"]

                if c in sp_ca:
                    c = sp_ca[c]

                if len(d) == 0:
                    l.append([a,c])
                else:
                            
                    for j in d:
                        e = j["species"]["name"]
                        if e in sp_ca:
                            e = sp_ca[e]
                        l.append([a,c,e])          
                            

        id_evolve[num] = l

        for i in l:
            for j in i:
                pk_id[j] = num
    except:
        print(num,"--------------------------------------------------------")
print(1)
# print(id_evolve)

# print(pk_id)
        
# getting all pokemon into JSON
filea = open('all.txt', 'r')
Lines = filea.readlines()
 
all_pokemon = dict()
all_pokemon_num = dict()

ap = []

for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])
    all_pokemon[b] = int(a)
    ap.append(b)
    all_pokemon_num[int(a)] = b


filea.close()

print(2)
lp = dict()
i = 1
for p in ap:
    print(i)
    try:
        c_d = dict()
        name = p

        l_name = p.lower()
        id = all_pokemon[name]
        evolve_id = pk_id[l_name]

        evolve_chain = id_evolve[evolve_id]

        c_d["Name"] = name
        c_d["ID"] = id
        c_d["Evolve_ID"] = evolve_id
        c_d["EvolveChain"] = evolve_chain

        evolve_from = []
        evolve_into = []

        for c in evolve_chain:
            for i in range(len(c)):
                if c[i] == l_name:
                    if i > 0:
                        evolve_from.append(c[i-1])
                    if i < len(c) - 1:
                        evolve_into.append(c[i+1])

        c_d["EvolveFrom"] = evolve_from
        c_d["EvolveInto"] = evolve_into
        c_d["Size"] = len(evolve_chain)

        lp[name.lower()] = c_d.copy()
    except:
        print(p)
    i += 1

print(3)
import json

with open('evolutionChains.json', 'w') as f:
    json.dump(lp, f)



    
