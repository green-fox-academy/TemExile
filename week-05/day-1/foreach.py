def plus_2(x):
    print(x+2)

def foreach(func, iterate):
    for _ in iterate:
        func(_)

foreach(plus_2, [1,2,3])
