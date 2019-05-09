m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]
m2 = [[4,3,2],
      [2,2,9],
      [2,5,7]]

m3 = [[1,3],[3,2]]
m4 = [[3,4],[1,1]]

# matrix addition
def matrix_add(a,b):
    d = []
    if len(a) != len(b) | len(a[0]) != len(b[0]):
        return print("They have different demension")
    for i in range(len(a)):
        c = [x + y for x, y in zip(a[i], b[i])]
        d.append(c)
    return d
print(matrix_add(m1,m2))
print(matrix_add(m3,m4))

# matrix substraction
def matrix_sub(a,b):
    d = []
    if len(a) != len(b) | len(a[0]) != len(b[0]):
        return print("They have different demension")
    for i in range(len(a)):
        c = [x - y for x, y in zip(a[i], b[i])]
        d.append(c)
    return d
print(matrix_sub(m1, m2))
print(matrix_sub(m3, m4))

# scale multiplication
def scale_mul(m,num):
    scale_list = [num] * len(m[0])
    d = []
    for i in range(len(m)):
        c = list(map(lambda x,y : x * y, scale_list, m[i]))
        #c = [x * y for x, y in map(m[i],scale_list)]
        d.append(c)
    return d
print(scale_mul(m1, 2))
print(scale_mul(m2, 3))

# Transposition
def transp(m):
    return list(map(list, zip(*m)))
print(transp(m1))






