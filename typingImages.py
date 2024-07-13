
import requests
import json


normalFrom = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]

typeSprites = dict()

for i in normalFrom:
    cur = dict()
    cur["Name"] = i
    cur["DisplayName"] = i.capitalize()
    cur["TypeLogoSquare"] = ""
    cur["TypeLogoCircle"] = ""
    cur["TypeTextSquare"] = ""
    cur["TypeTextRound"] = ""
    cur["TypeTextLogo"] = ""
    typeSprites[i] = cur
    

with open('allTypeLogos.json', 'w') as f:
    json.dump(typeSprites, f)

