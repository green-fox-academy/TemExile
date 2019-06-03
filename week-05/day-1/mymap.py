def plus_2(x):
    return x+2

def mymap(func, itera):
    out_list = []
    for _ in itera:
        out_list.append(func(_))
    return out_list

print(mymap(plus_2, [1,2,3]))
