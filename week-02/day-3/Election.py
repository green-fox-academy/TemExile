
def election(file):
    a = open(file, 'r')
    b = a.readlines()
    a.close()
    c = []
    for line in b:
        d = line.split(',')
        c.append(d)
    e = []
    for i in range(len(c)):
        if '' in c[i]:
            print(c[i])
        else:
            e.append(c[i])
    return e


print(election('election.csv'))