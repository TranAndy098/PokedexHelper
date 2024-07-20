import json

f = open('allTypeData.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

f = open('APIToDisplay2.json')
data2 = json.load(f) #list of dictionary of pokemon data
f.close()

typing = list(data.keys())
pokemon_Types = dict()



for i in typing:
    for mon in data[i]["Pokemon"]:
        if mon not in pokemon_Types:
            pokemon_Types[mon] = [i]
        else:
            pokemon_Types[mon].append(i)

pokemon_Types_order = dict()
national = dict()
pokemon = list(data2.keys())

br = False

for mon in pokemon:
    if (mon == "venusaur-mega"):
        br = True

    if mon in pokemon_Types:

        if not br:
            national[mon] = pokemon_Types[mon]
        pokemon_Types_order[mon] = pokemon_Types[mon]



with open('nationalPokedexTyping.json', 'w') as f:
    json.dump(national, f)



with open('pokemonTypingChart.json', 'w') as f:
    json.dump(pokemon_Types_order, f)
