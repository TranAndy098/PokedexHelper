
import requests
import json

f = open('AllTypeLogos.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

types = list(data.keys())



for i in types:
    cur = data[i]

    fields = list(cur.keys())

    name = cur["DisplayName"]

    for j in range(2,len(fields)):
        print(i, j)

  
        place = f"/typeImages/{i}/{name}{fields[j]}.png"
 
        data[i][fields[j]] = place


with open('allTypeLogos.json', 'w') as f:
    json.dump(data, f)