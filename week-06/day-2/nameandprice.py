def get_name(item):
    b = list(item)
    c = list(b[1])
    d = list(c[5])
    e = list(d[3])
    return e[0]

def get_price(item):
    b = list(item)
    c = list(b[3])
    if len(c) == 11:
        d = list(c[1])
        e = list(d[1])
        current_price = list(e[3])[0]
        f = list(e[1])
        if len(f) == 1:
            previous_price = current_price
        else:
            previous_price = list(f[3])[0]
        return [previous_price, current_price]
    elif len(c) == 13:
        d = list(c[3])
        e = list(d[1])
        current_price = list(e[3])[0]
        f = list(e[1])
        if len(f) == 1:
            previous_price = current_price
        else:
            previous_price = list(f[3])[0]
        return [previous_price, current_price]