def readtolist(infile):
    import csv
    with open(infile, 'r') as rawdata:
        data1 = rawdata.readlines()
    raw_list = []
    for line in data1:
        line = line[:-2]
        line = line.split(',')
        raw_list.append(line)
    use_list = []
    for l1 in raw_list:
        a = l1
        b = a[1]
        c = b[:10]
        d = b[12:]
        used = [c, d, a[5], a[7]]
        use_list.append(used)
    return use_list

use_list = readtolist('logs.csv')

door_set = set()
for line in use_list:
    door_set.add(line[2])
door_list = list(door_set)
door_dic = {}
for door in door_list:
    door_dic[door] = 'not entrance'
door_dic['A66 - 04 F??BEJ??RAT (F-1) Door #1'] = 'main'
door_dic['A66 - 12 Recepci?? (2-1) Door #1'] = 'second'
door_dic['A66 - 18 El??t??r 316 (3-2) Door #1'] = 'third'

main_door_log = {}
for line in use_list:
    date, time, door, name = line
    if door_dic[door] == 'main' or door_dic[door] == 'second' or door_dic[door] == 'third':
        enter_record = [time, door]
        if name not in main_door_log:
            main_door_log[name] = {date:[enter_record]}
        else:
            if date in main_door_log[name]:
                main_door_log[name][date].append(enter_record)
            else:
                main_door_log[name][date] = [enter_record]

enter_log = {}
for line in use_list:
    date, time, door, name = line
    enter_record = [time, door]
    if name not in enter_log:
        enter_log[name] = {date:[enter_record]}
    else:
        if date in enter_log[name]:
            enter_log[name][date].append(enter_record)
        else:
            enter_log[name][date] = [enter_record]

enter_time = {}
for name in enter_log.keys():
    for date in enter_log[name].keys():
        if name in enter_time:
            enter_time[name].append(enter_log[name][date][0][0])
        else:
            enter_time[name] = [enter_log[name][date][0][0]]

log_day_count = {}
for key in enter_time:
    log_day_count[key] = len(enter_log[key])

main_door_time = {}
for name in main_door_log.keys():
    for date in main_door_log[name].keys():
        if name in main_door_time:
            main_door_time[name].append(main_door_log[name][date][0][0])
        else:
            main_door_time[name] = [main_door_log[name][date][0][0]]

day_counts = {}
for key in main_door_time:
    day_counts[key] = len(main_door_log[key])


