
import requests
import json

f = open('AllTypeLogos.json')
data = json.load(f) #list of dictionary of pokemon data
f.close()

types = list(data.keys())


import os

for i in types:
    folder_path = f"./typeImages/{i}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")


for i in types:
    cur = data[i]

    fields = list(cur.keys())

    name = cur["DisplayName"]

    for j in range(2,len(fields)):
        print(i, j)

        url = cur[fields[j]]

        data2 = requests.get(url).content 
  
        f = open(f"./typeImages/{i}/{name}{fields[j]}.png",'wb') 
 
        f.write(data2) 
        f.close() 
