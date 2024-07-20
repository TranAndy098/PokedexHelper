import json

f = open('pokemonGameLocations.json')
gameLocations = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('gamesPerGen.json')
gamesPerGen = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('gen.json')
pokemonPerGen = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('displayToAPI.json')
disToAPI = json.load(f) #list of dictionary of pokemon data
f.close()


pokemonToGen = dict()


for i in range(len(pokemonPerGen)):
    for pokemon in pokemonPerGen[i]:

        pokemonToGen[disToAPI[pokemon]] = i

pokemons = list(disToAPI.values())


new_gameLocations = dict()

for pokemon in pokemons:
    new_gameLocations[pokemon] = dict()

for pokemon in pokemons:
    pkFirstGen = pokemonToGen[pokemon]
    if pokemon in gameLocations:
        for i in range(1, 10):
            if i >= pkFirstGen:
                for game in gamesPerGen[str(i)]:
                    if game in gameLocations[pokemon]:
                        new_gameLocations[pokemon][game] = gameLocations[pokemon][game]


with open('pokemonLocationsPerGame.json', 'w') as f:
    json.dump(new_gameLocations, f)

