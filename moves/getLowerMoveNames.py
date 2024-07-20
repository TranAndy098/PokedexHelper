import json

f = open('moveDisplayToAPI.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

data2 = data.copy()



for i in data2.keys():
    data[i.lower()] = data[i]
    

with open('movesDisplauPAIlower.json', 'w') as f:
    json.dump(data, f)

