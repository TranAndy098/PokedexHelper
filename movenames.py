import json
f = open('allAPIMoves.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

d = dict()
c = dict()
moves = []

for i in data.keys():
    Realname = data[i]["realName"]
    d[Realname] = i
    c[i] = Realname
    moves.append(Realname)
    

with open('realMoveToAPI.json', 'w') as f:
    json.dump(d, f)

moves.sort()

with open('realMoveNames.json', 'w') as f:
    json.dump(moves, f)
with open('APItorealMove.json', 'w') as f:
    json.dump(c, f)