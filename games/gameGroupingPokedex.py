
import requests
import json

f = open('gamesAPITODisplay.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()


game = list(data.keys())


f = open('APIToDisplay.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

pokemons = list(data.keys())

f = open('pokedexPerGameReplaces.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()



games_pokedex = dict()


replace = dict()

# for all regular locaiton-area
for i in range(1,34):
    print(i, "/", 33)
    if i != 10:
    

        response = requests.get(f"https://pokeapi.co/api/v2/pokedex/{i}")
        response = response.json()

        pokemon_entries = response["pokemon_entries"]
        pokedexname= response["name"]

        ver_groups = response["version_groups"]

        for v in ver_groups:
            vname, vurL = list(v.keys())
            vname = v[vname]
            vurL = v[vurL]

            response = requests.get(vurL)
            response = response.json()

            versions = response["versions"]

            for ver in versions:
                name, urL = list(ver.keys())
                name = ver[name]
                urL = ver[urL]

                if name not in games_pokedex:
                    games_pokedex[name] = dict()

                if pokedexname not in games_pokedex[name]:
                
                    games_pokedex[name][pokedexname] = dict()

                for mon_enmtry in pokemon_entries:
                    num = mon_enmtry["entry_number"]
                    mon = mon_enmtry["pokemon_species"]["name"]

                    if mon not in pokemons:

                        replace[mon] = ""
                        mon = data[mon]
                    
                    games_pokedex[name][pokedexname][num] = mon
                

                




with open('pokedexPerGame.json', 'w') as f:
    json.dump(games_pokedex, f)

with open('pokedexPerGameReplaces2.json', 'w') as f:
    json.dump(replace, f)


