
import requests
import json


locations_per_games = dict()



response = requests.get("https://pokeapi.co/api/v2/version-group/?limit=30")
response = response.json()

game_groups = response["results"]

for game in game_groups:
    name, urL = list(game.keys())
    name = game[name]

    locations_per_games[name] = []


num = 1

# for all regular locaiton-area
for i in range(1,11):
    print(num, "/", 10)
    response = requests.get(f"https://pokeapi.co/api/v2/region/{i}/")
    response = response.json()

    locations = response["locations"]
    version_groups = response["version_groups"]


    for location in locations:
        area, urL = list(location.keys())
        area = location[area]
        urL = location[urL]
        response = requests.get(urL)
        response = response.json()
        areas = response["areas"]
        for thing in areas:
            area2, ur = list(thing.keys())
            area2 = thing[area2]
            for version in version_groups:
                v, u = list(version.keys())
                v = version[v]
                locations_per_games[v].append(area2)
    
    num += 1


locations_per_game = dict()


for game in game_groups:
    name, urL = list(game.keys())
    name = game[name]
    urL = game[urL]
    response = requests.get(urL)
    response = response.json()

    versions = response["versions"]
    for version in versions:
        g, urL = list(version.keys())
        g = version[g]

        locations_per_game[g] = locations_per_games[name].copy()




with open('locationsPerGame.json', 'w') as f:
    json.dump(locations_per_game, f)


