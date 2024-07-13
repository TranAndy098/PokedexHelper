
filea = open('all.txt', 'r')
Lines = filea.readlines()

ap = []

for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])

    ap.append(b)

filea.close()

apip= []

d = dict()
import requests
for i in range(1, 1026):
    print(i)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    response = response.json()
    d[ap[i-1].lower()] = response["name"]




import json

with open('allToAPI.json', 'w') as f:
    json.dump(d, f)

