m1 = [[1,2,3], [4,5,6], [7,8,9]]
m2 = [[4,3,2], [2,2,9], [2,5,7]]
m3 = [[1,3], [3,2]]
m4 = [[3,4], [1,1]]
m5 = m1*3
m6 = m3*4

# matrix addition
def matrix_add(a,b):
    d = []
    if len(a) != len(b) | len(a[0]) != len(b[0]):
        return "They have different demension"
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
        return "They have different dimensions"
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
def tran(m):
    a = []
    for i in range(len(m)):
        b = []
        for j in range(len(m)):
            b.append(m[j][i])
        a.append(b)
    return a
print(tran(m1))

# Transposition_faster
def transp(m):
    return list(map(list, zip(*m)))
print(transp(m1))

# multiplication
def mul(m,n):
    if len(m[0]) != len(n):
        return "You cannot do multiplication for this two matrices"
    else:
        a = []
        for i in range(len(m)):
            b = []
            for j in range(len(n[0])):
                c = 0
                for k in range(len(m[0])):
                    c = c + m[i][k] * n[k][j]
                b.append(c)
            a.append(b)
        return a
print(mul(m1, m2))
print(mul([[1,2,3],[3,2,1]],[[1,2],[3,4],[2,1]]))

# horizontal flipping
def h_flip(m):
    if len(m)%2 == 0:
        a = len(m) // 2
        b = m[:a]
        c = m[a:]
        return c+b
    elif len(m)%2 != 0:
        a = len(m) // 2
        b = m[:a]
        c = m[a+1:]
        return c+[m[a]]+b
print(h_flip(m5))
print(h_flip(m6))

# vertical flipping
def v_flip(m):
    a = []
    for i in range(len(m)):
        b = m[i]
        c = b[::-1]
        a.append(c)
    return a
print(v_flip(m5))

# main anti-diagonal mirroring
def anti_dia(m):
    if len(m) != len(m[0]):
        return "This mattrix is not a square matrix"
    else:
        a = transp(m)
        b = h_flip(a)
        c = v_flip(b)
        return c
print(anti_ia(m1))

# matrix rotation
def rotate(m, cl = 'clockwise'):
    if cl == 'clockwise':
        a = transp(m)
        b = h_flip(a)
        return b
    elif cl == 'anti':
        a = transp(m)
        b = v_flip(a)
        return b
print(rotate(m1, 'anti'))
print(rotate(m1, 'clockwise'))

# rotation with multiplication of 90 degree
def rotate_n(m, n = 0, cl = 'clockwise'):
    re = n%4
    a = m
    if re == 0:
        return a
    else:
        for i in range(1,re+1):
            a = rotate(a)
        return a
print(rotate_n(m1, n = 3, cl = 'clockwise'))
print(rotate_n(m1, n = 1, cl = 'anti'))












