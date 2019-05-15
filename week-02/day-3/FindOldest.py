# oldest movie
def findoldest(file):
    a = open(file, 'r')
    b = a.readlines()
    c = []
    for line in b:
        d = line.split(';')
        c.append(d)
    e = []
    for i in range(len(c)):
        e.append(int(c[i][1]))
        f = e.index(min(e))
    return c[f][0]


print(findoldest('movies.csv'))
