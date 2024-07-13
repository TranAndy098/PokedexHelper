
import requests
import json

f = open('displayToAPI.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

mons = list(data.keys())


for i in mons:
    
    newName = i.lower()

    data[newName] = data[i]

    


with open('twicdeDisAPI.json', 'w') as f:
    json.dump(data, f)



    
