from data_m_person_count import readtolist
import matplotlib.pyplot as plt
from Time_to_Sec import timetosec
from Time_to_Sec import sectotime
from workday import workday
from doorlist import maindoor
import numpy as np

use_list = readtolist('logs.csv')
door_list = maindoor()
day_list = workday()

date_name_time = {}
for line in use_list:
    date, time, door, name = line
    sec = timetosec(time)
    enter_record = [sec, door]
    if door in door_list and date in day_list:
        if date not in date_name_time:
            date_name_time[date] = {name:[enter_record]}
        else:
            if name in date_name_time[date]:
                date_name_time[date][name].append(enter_record)
            else:
                date_name_time[date][name] = [enter_record]


        