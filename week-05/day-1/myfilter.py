def is_odd(x):
    return x%2 != 0

def myfilter(func, iterate):
    out_list = []
    for _ in iterate:
        if func(_):
            out_list.append(_)
    return out_list
print(myfilter(is_odd, [1,2,3]))