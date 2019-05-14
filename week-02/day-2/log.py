import re
def findIP(file):
    a = open(file, 'r')
    b = a.readlines()
    c = []
    paten = re.compile('\d\d\.\d\d\.\d\d\.\d\d')
    for i in range(len(b)):
        d = paten.search(b[i])
        c.append(d.group())
    return c
ss = findIP('log.txt')
print(ss)

def findratio(file):
    a = open(file, 'r')
    b = a.readlines()
    c = []
    for lines in b:
        line = lines.split()
        c.append(line[6])
    return c.count("GET")/c.count("POST")

print(findratio('log.txt'))


