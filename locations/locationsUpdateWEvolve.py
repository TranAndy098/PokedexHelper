import json

f = open('evolutionChains.json')
evolutions = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('pokemonGameLocations.json')
locations = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('APIToDisplay.json')
pokemons2 = json.load(f) #list of dictionary of pokemon data
f.close()

pokemons = list(pokemons2.keys())


for pokemon in pokemons:
    if pokemon in evolutions:
        for preevo in evolutions[pokemon]["EvolveFrom"]:
            if preevo in locations:
                games = list(locations[preevo].keys())
                for game in games:
                    if pokemon not in locations:
                        locations[pokemon] = dict()

                    


                    if game not in locations[pokemon]:
                        locations[pokemon][game] = dict()
                        locations[pokemon][game]["evolutions"] = preevo

with open('pokemonGameLocations2.json', 'w') as f:
    json.dump(locations, f)