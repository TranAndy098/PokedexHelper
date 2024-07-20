
import requests
import json

f = open('gamesAPIToDisplay.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

logos = dict()

for i in list(data.keys()):
    logos[i] = f"{i}.ico"




with open('gamesLogos.json', 'w') as f:
    json.dump(logos, f)


# for all palpark locaitons

