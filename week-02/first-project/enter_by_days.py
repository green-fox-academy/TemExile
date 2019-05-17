from data_m_person_count import readtolist

use_list = readtolist('logs.csv')

date_name_time = {}
for line in use_list:
    date, time, door, name = line
    enter_record = [time, door]
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
print(people_count)