import csv

def high_ratio(file):
    exam_list = []
    with open(file) as tsv:
        fe = csv.reader(tsv, delimiter = '\t')
        for line in fe:
            exam_list.append(line)
    exam_list = exam_list[1:]
    time_list = []
    for i in range(len(exam_list)):
        time_list.append(exam_list[i][2])
    min_list = []
    for j in range(len(time_list)):
        if 'h' in time_list[j] and 's' not in time_list[j] and 'm' not in time_list[j]:
            if '.' in time_list[j]:
                time_p = time_list[j]
                time_l = int(time_p[time_p.find('.')+1:time_p.find('h')])/10
                f_time = time_l * 60
                min_list.append(f_time)
            else:
                time_p = time_list[j]
                f_time = int(time_p[:time_p.find('h')]) * 60
                min_list.append(f_time)
        elif 'h' not in time_list[j] and 's' in time_list[j] and 'm' not in time_list[j]:
            time_p = time_list[j]
            f_time = int(time_p[:time_p.find('s')]) / 60
            min_list.append(f_time)
        elif 'h' not in time_list[j] and 's' not in time_list[j] and 'm' in time_list[j]:
            time_p = time_list[j]
            time_l = int(time_p[:time_p.find('m')])
            min_list.append(int(time_l))
        elif 'h' in time_list[j] and 's' in time_list[j] and 'm' in time_list[j]:
            time_p = time_list[j]
            hh = int(time_p[:time_p.find('h')]) * 60
            mm = int(time_p[time_p.find('h')+1:time_p.find('m')])
            ss = int(time_p[time_p.find('m')+1:time_p.find('s')]) / 60
            f_time = hh + mm + ss
            min_list.append(f_time)
        elif 'll' in time_list[j]:
            min_list.append(int('9999'))
        elif ':' in time_list[j]:
            time_p = time_list[j]
            time_l = time_p.split(':')
            hh = int(time_l[0]) * 60
            mm = int(time_l[1])
            ss = int(time_l[2]) / 60
            f_time = hh + mm + ss
            min_list.append(f_time)
    eff = []
    for k in range(len(min_list)):
        ratio = int(exam_list[k][1]) / min_list[k]
        eff.append(ratio)
    eff_ratio = max(eff)
    users = eff.index(eff_ratio)
    print(f'The {users + 1}th user get the highest ratio, {eff_ratio}')


high_ratio('exams.tsv')
