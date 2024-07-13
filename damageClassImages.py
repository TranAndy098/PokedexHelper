
import requests
import json


normalFrom = ["status", "physical", "special"]

damageSprites = dict()

for i in normalFrom:
    cur = dict()
    cur["Name"] = i
    cur["DisplayName"] = i.capitalize()
    cur["TypeLogoBW"] = ""
    cur["TypeLogoXY"] = ""
    cur["TypeLogoBDSP"] = ""
    damageSprites[i] = cur
    

with open('allDamageClassLogos.json', 'w') as f:
    json.dump(damageSprites, f)

