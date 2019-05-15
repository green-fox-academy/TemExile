import json
import csv


def wt_json(file1, file2):
    infile = open(file1, 'r')
    content = csv.DictReader(infile)

    full_list = []
    for row in content:
        dic = {}
        for key, value in row.items():
            dic[key] = value
        full_list.append(dic)
    infile.close()
    with open (file2, 'w') as outfile:
        json.dump(full_list, outfile)


wt_json('users.csv', 'users.json')