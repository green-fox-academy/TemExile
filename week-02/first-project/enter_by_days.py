from data_m_person_count import readtolist
from doorlist import maindoor
from workday import workday

use_list = readtolist('logs.csv')
door_list = maindoor()
day_list = workday()

date_name_time = {}
for line in use_list:
    date, time, door, name = line
    enter_record = [time, door]
    if door in door_list and date in day_list:
        if date not in date_name_time:
            date_name_time[date] = {name:[enter_record]}
        else:
            if name in date_name_time[date]:
                date_name_time[date][name].append(enter_record)
            else:
                date_name_time[date][name] = [enter_record]

people_count = {}
for key in date_name_time.keys():
    people_count[key] = len(date_name_time[key])

first_enter = {}
for key in date_name_time.keys():
    for name in date_name_time[key].keys():
        if name in first_enter:
            first_enter[name].append(date_name_time[key][name][0][0])
        elif name not in first_enter:
            first_enter[name] = [date_name_time[key][name][0][0]]
