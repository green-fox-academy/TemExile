def get_dtname(item):
    a = list(item)
    b = list(a[1])
    c = b[0]
    c = c[2:]
    d = c.strip()
    return d

def get_dtprice(item):
    a = list(item)
    b = list(a[1])
    c = list(b[1])
    d = list(c[5])
    e = list(d[5])
    return e[0]
