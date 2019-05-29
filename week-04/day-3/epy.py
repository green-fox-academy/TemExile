import json
import xml.etree.ElementTree as et
import psycopg2

# csv to list
with open('employees.csv', 'r') as csvinfile:
    cfile = csvinfile.readlines()
csv_data = cfile[1:]
csvdata = []
for i in csv_data:
    i = i[:-1]
    a = i.split(',')
    age = 2019 - int(a[3][-4:])
    salary = int(a[5]) * 12
    person = [a[1], a[2], a[4], age, salary]
    csvdata.append(person)

# json to list
with open('employees.json', 'r') as jsoninfile:
    jfile = json.load(jsoninfile)
jsondata = []
for i in jfile:
    a = i
    if a['monthly_salary'] == None:
        a['monthly_salary'] = 0
    name = a['name'].split()
    first = name[0]
    last = name[1]
    age = 2019 - int(a['birth_date'][-4:])
    salary = 12 * int(a['monthly_salary'])
    person = [first, last, a['gender'], age, salary]
    jsondata.append(person)

# xml to list
tree = et.parse('employees.xml')
root = tree.getroot()
xmldata = []
for p in root:
    per = []
    for dat in p:
        per.append(dat.text)
    xmldata.append(per)
xml_data = []
for i in xmldata:
    name = i[1].split()
    first = name[0]
    last = name[1]
    age = 2019 - int(i[2][:4])
    person = [first, last, i[4], age, int(i[5])]
    xml_data.append(person)

full_data = csvdata + jsondata + xml_data

# Write to database
connection = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'wengleo'
)
cursor = connection.cursor()
insert_dat = 'INSERT INTO employee_day_3 (first_name, last_name, gender, age, salary) VALUES(%s, %s, %s, %s, %s)'
for i in full_data:
    cursor.execute(insert_dat, i)
    connection.commit()