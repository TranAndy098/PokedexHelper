
import requests
import json

response = requests.get("https://pokeapi.co/api/v2/location-area/?limit=1054")
response = response.json()

# list of all locaitons with api name an durl 
allPlaces = response["results"]

pokemonGameLocationMethod = dict()
locationGamePokemon = dict()

num = 1

# for all regular locaiton-area
for i in allPlaces:
    print(num, "/", 1054)
    name, urL = list(i.keys())
    name = i[name]
    urL = i[urL]


    response = requests.get(urL)
    response = response.json()

    locationName = response["name"]

    allEncounters = response["pokemon_encounters"]


    if locationName not in locationGamePokemon:
        locationGamePokemon[locationName] = dict()


    for encounterNum in range(len(allEncounters)):

        pokemon = allEncounters[encounterNum]["pokemon"]["name"]
        if pokemon not in pokemonGameLocationMethod:
            pokemonGameLocationMethod[pokemon] = dict()

        for versionDetail in range(len(allEncounters[encounterNum]["version_details"])):

            maxChance = allEncounters[encounterNum]["version_details"][versionDetail]["max_chance"]
            gameVersion = allEncounters[encounterNum]["version_details"][versionDetail]["version"]["name"]



            if gameVersion not in pokemonGameLocationMethod[pokemon]:
                pokemonGameLocationMethod[pokemon][gameVersion] = dict()

            if locationName not in pokemonGameLocationMethod[pokemon][gameVersion]:
                pokemonGameLocationMethod[pokemon][gameVersion][locationName] = dict()



            if gameVersion not in locationGamePokemon[locationName]:
                locationGamePokemon[locationName][gameVersion] = dict()
            
            if pokemon not in locationGamePokemon[locationName][gameVersion]:
                locationGamePokemon[locationName][gameVersion][pokemon] = dict()


            for encounterDetail in range(len(allEncounters[encounterNum]["version_details"][versionDetail]["encounter_details"])):

                encounterMethod = dict()
                pokemonEncounter = dict()

                minLevel = allEncounters[encounterNum]["version_details"][versionDetail]["encounter_details"][encounterDetail]["min_level"]
                maxLevel = allEncounters[encounterNum]["version_details"][versionDetail]["encounter_details"][encounterDetail]["max_level"]
                chance = allEncounters[encounterNum]["version_details"][versionDetail]["encounter_details"][encounterDetail]["chance"]
                methodName = allEncounters[encounterNum]["version_details"][versionDetail]["encounter_details"][encounterDetail]["method"]["name"]

                encounterMethod["MinLevel"] = minLevel
                encounterMethod["MaxLevel"] = maxLevel
                encounterMethod["Chance"] = chance
                encounterMethod["Conditions"] = []

                pokemonEncounter["MinLevel"] = minLevel
                pokemonEncounter["MaxLevel"] = maxLevel
                pokemonEncounter["Chance"] = chance
                pokemonEncounter["Method"] = methodName
                


                for conditionValue in range(len(allEncounters[encounterNum]["version_details"][versionDetail]["encounter_details"][encounterDetail]["condition_values"])):
                    condtionName = allEncounters[encounterNum]["version_details"][versionDetail]["encounter_details"][encounterDetail]["condition_values"][conditionValue]["name"]
                    encounterMethod["Conditions"].append(condtionName)

                if methodName not in pokemonGameLocationMethod[pokemon][gameVersion][locationName]:
                    pokemonGameLocationMethod[pokemon][gameVersion][locationName][methodName] = dict()

                pokemonGameLocationMethod[pokemon][gameVersion][locationName][methodName] = encounterMethod
                locationGamePokemon[locationName][gameVersion][pokemon] = pokemonEncounter
    num += 1


with open('pokemonGameLocations.json', 'w') as f:
    json.dump(pokemonGameLocationMethod, f)

with open('locationGamePokemon.json', 'w') as f:
    json.dump(locationGamePokemon, f)


# for all palpark locaitons

