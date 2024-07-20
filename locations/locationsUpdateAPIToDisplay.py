import json

f = open('locationNamesAPIToDisplay.json')
locations2 = json.load(f) #list of dictionary of pokemon data
f.close()



locations = list(locations2.keys())

disAPI = dict()
APIdis = dict()

def correctName(apiName):
    components = apiName.split("-")
    for i in range(len(components)):
        components[i] = components[i].capitalize()
    return " ".join(components)

def correctNameA(apiName):
    components = apiName.split("-")
    s = []
    for i in range(len(components)):
        if components[i] != "area":
            s.append(components[i].capitalize())
    return " ".join(s)

num = 1

# for all regular locaiton-area
for i in locations:
    print(num, "/", 1054)
    name = i

    if "area-zero" in name:
        Display = correctName(name)
    elif "area-one" in name:
        Display = correctName(name)
    elif "area-two" in name:
        Display = correctName(name)
    elif "area-three" in name:
        Display = correctName(name)
    elif "area-four" in name:
        Display = correctName(name)
    elif "area-five" in name:
        Display = correctName(name)
    elif "area-six" in name:
        Display = correctName(name)
    else:
        Display = correctNameA(name)


    
    disAPI[Display] = name
    APIdis[name] = Display


    num += 1


with open('locationNamesAPIToDisplay2.json', 'w') as f:
    json.dump(APIdis, f)

with open('locationNamesDisplayToAPI2.json', 'w') as f:
    json.dump(disAPI, f)

