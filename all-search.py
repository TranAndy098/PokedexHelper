
filea = open('all.txt', 'r')
Lines = filea.readlines()

ap = []

for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])

    ap.append(b)

filea.close()

import json
f = open('allToAPI.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

apipoke = list(data.values())


print(apipoke)

displayToAPI = dict()
APIToDisplay = dict()


for i in range(1025):
    displayToAPI[ap[i]] = apipoke[i]
    APIToDisplay[apipoke[i]] = ap[i]


with open('displayToAPI.json', 'w') as f:
    json.dump(displayToAPI, f)

with open('APIToDisplay.json', 'w') as f:
    json.dump(APIToDisplay, f)


    
