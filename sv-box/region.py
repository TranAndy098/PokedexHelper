
"""
# getting all unobtainable pokemon
fileu = open('un.txt', 'r')
Lines = fileu.readlines()
 
unobtainable = []

for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])
    unobtainable.append(int(a))

fileu.close()



# getting all obtainable pokemon
fileo = open('ob.txt', 'r')
Lines = fileo.readlines()
 
obtainable = []

for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])
    obtainable.append(int(a))

fileo.close()
"""

# getting all pokemon
filea = open('all.txt', 'r')
Lines = filea.readlines()
 
all_pokemon = dict()
all_pokemon_num = dict()

for line in Lines:
    l = line.strip()
    a = l.split(" ")[0]
    b =  " ".join(l.split(" ")[1:])
    all_pokemon[b] = int(a)
    all_pokemon_num[int(a)] = b

filea.close()

# getting boxes
filea = open('box.txt', 'r')
Lines = filea.readlines()
 
boxes = dict()
box_comp = dict()

for line in Lines:
    l = line.strip()
    a, b, c = l.split(" ")
    boxes[int(a)] = [int(b), int(c)]

    if b in box_comp:
        box_comp[b].append(int(a))
    else:
        box_comp[b] = [int(a)]
   

filea.close()

# getting found pokemon
filea = open('found.txt', 'r')
Lines = filea.readlines()
 
found_pokemon = dict()

for line in Lines:
    l = line.strip().split(" ")
    b = l[-1:][0]
    a = " ".join(l[:-1])
    found_pokemon[a] = b
    

filea.close()

"""
for p in all_pokemon.keys():
    num = all_pokemon[p]
    if num in boxes:
        print(p, num, boxes[int(num)][0], boxes[int(num)][1])
    else:
        print(p, num, "Unobtainable")
"""


box_nums = ["2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]


def print_box(num_str):

    i = 0
    rows = "----- Box " + num_str + " -----"
    print(rows)

    rows = ""
    for n in box_comp[num_str]:
        if i % 6 == 0:
            rows += "| "
        rows += all_pokemon_num[n] + " | "
        i += 1
        if i % 6 == 0:
            rows += "\n"
    print(rows)


def update_found(status, pokemon):

    found_pokemon[pokemon] = status

    filea = open('found.txt', 'w')
    summary = ''

    # write each entry to string and then write to text and save to dictionary
    for pokemon in found_pokemon:
        summary += pokemon + " " + found_pokemon[pokemon] +"\n"

    filea.write(summary)
    filea.close()


def print_missing():
    summary = ''
    print("-----Not Found-----")
    for pokemon in found_pokemon:
        num = all_pokemon[pokemon]
        if num in boxes:
            if found_pokemon[pokemon] == "False":
                statement = f'{pokemon} | Dex: {num} | Box: {boxes[int(num)][0]} | Spot: {boxes[int(num)][1]}'
                print(statement)
                summary += statement + "\n"
    print("-------------------")

    filea = open('missing.txt', 'w')
    filea.write(summary)
    filea.close()


def update_missing():
    missing_spots = dict()
    for i in box_nums:
        cur = []
        spots = input(f'Box {i}, Which spots are missing: ').strip()
        if spots == 'quit':
            return
        spot_list = spots.strip().split(" ")
        for n in spot_list:
            if len(n) > 0:
                cur.append(int(n))
        missing_spots[int(i)] = cur
    
    for pokemon in found_pokemon:
        num = all_pokemon[pokemon]
        if num in boxes:
            b = boxes[int(num)][0]
            s = boxes[int(num)][1]
            if s in missing_spots[b]:
                found_pokemon[pokemon] = "False"
            else:
                found_pokemon[pokemon] = "True" 
    
    filea = open('found.txt', 'w')
    summary = ''

    # write each entry to string and then write to text and save to dictionary
    for pokemon in found_pokemon:
        summary += pokemon + " " + found_pokemon[pokemon] +"\n"

    filea.write(summary)
    filea.close()



pokemon = input("Enter pokemon name, box number, print, f, m, allm, updatem, quit: ").strip()
while pokemon != "quit":
    if pokemon == "print":
        for i in box_nums:
            print_box(i)
    elif pokemon == "f":
        pokemon = input("Enter pokemon name: ").strip()
        update_found("True", pokemon)
    elif pokemon == "m":
        pokemon = input("Enter pokemon name: ").strip()
        update_found("False", pokemon)
    elif pokemon == "allm":
        print_missing()
    elif pokemon == "updatem":
        update_missing()
    elif pokemon in box_nums:
        print_box(pokemon)
    elif pokemon in all_pokemon:
        num = all_pokemon[pokemon]
        if num in boxes:
            update_found("True", pokemon)
            print("Dex:", num, "| Box:", boxes[int(num)][0], "| Spot:", boxes[int(num)][1])
        else:
            print("| Dex:", num, "is Unobtainable")
    else:
        print("Not valid option")
    pokemon = input("Enter pokemon name, box number, print, f, m, allm, updatem, quit: ").strip()


