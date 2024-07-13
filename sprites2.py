import json
f = open('certainForms.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()



for i in data:
    for j in range(len(data[i])):
        for k in data[i][j]:
            n = data[i][j][k]["DisplayName"]
            data[i][j][k]["DisplayName"] = n + " " + i.capitalize()
            data[i][j][k]["DisplayTitle"] = n



with open('certainForms2.json', 'w') as f:
    json.dump(data, f)
