
filea = open('all.txt', 'r')
Lines = filea.readlines()

ap = []
cur = []
starts = ["Chikorita", "Treecko", "Turtwig", "Victini", "Chespin", "Rowlet", "Grookey", "Sprigatito"]

print(1)
for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])

    if b in starts:
        ap.append(cur)
        cur = []
    
    cur.append(b)

filea.close()

print(2)

lp = []
i = 1
for p in ap:
    d =dict()
    d["Generation"] = i
    d["Pokemon"] = p
    i+=1
    lp.append(d.copy())
    

print(3)
import json

with open('gen.json', 'w') as f:
    json.dump(ap, f)



    
