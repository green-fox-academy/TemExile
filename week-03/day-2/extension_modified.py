def add(a, b):
    return a + b

def max_of_three(a, b, c):
    num = [a, b, c]
    num = sorted(num)
    return num[-1]

def median(pool):
    num = sorted(pool)
    if len(num) % 2 == 0:
        return (num[len(num)/2 - 1] + num[len(num)/2])/2
    else:
        return num[len(num)//2]  

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = list(hungarian)
    new = []
    for char in teve:
        if is_vovel(char):
            char = char + 'v' + char
            new.append(char)
        else:
            new.append(char)
    newword = ''.join(new)
    return newword

