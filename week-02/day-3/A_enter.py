import csv

with open('logs.csv', 'r') as rawfile:
    data1 = rawfile.readlines()

raw_list = []
for line in data1:
    line = line[:-2]
    line = line.split(',')
    raw_list.append(line)

relist = []
for l1 in raw_list:
    a = l1
    b = a[1]
    c = b[:10]
    d = b[12:]
    e = [c, d, a[5], a[-1]]
    relist.append(e)

doorset = set()
for ll in relist:
    doorset.add(ll[2])

maindoor = 'A66 - 04 F脮BEJ脕RAT (F-1) Door #1'

door_enter = []
for a in relist:
    if maindoor in a:
        door_enter.append(a)

enterdic = {}
for line in door_enter:
    date, time, door, card = line
    if card not in enterdic:
        enterdic[card] = {date:[time]}
    else:
        if date in enterdic[card]:
            enterdic[card][date].append(time)
        else:
            enterdic[card][date] = [time]

entercount = {}
for key in enterdic.keys():
    entercount[key] = 0
    carddic = {}
    for date in enterdic[key].keys():
        carddic[date] = len(enterdic[key][date])
        entercount[key] = carddic




