# doubling
base_number = 123
def doubling(n):
    n = n*2
    return n
print(doubling(base_number))

# greeting
al = "Greenfox"
def greet(name):
    print(f"Greetings, dear {name}")
greet("Greefox")

# append_a
typo = "Chinchill"
def append_a_func(str):
    str = str+"a"
    return str
print(append_a_func(typo))

# summing
def summing(n):
    a = []
    for i in range(n+1):
        a.append(i)
    return sum(a)
print(summing(5))

# factorio
def fac(n):
    a = 1
    for i in range(1,n):
        a = a * i
    return a * n
print(fac(3))

# print_params
def print_params(*args):
    print(args)
print_params(1,2,3,"asdf")

# subint
def subint(num, ls):
    str1 = str(num)
    a = []
    for i in range(len(ls)):
        if str1 in str(ls[i]):
            a.append(i)
    return a
print(subint(1, [1, 11, 34, 52, 61]))
print(subint(9, [1, 11, 34, 52, 61]))

# unique
list1 = [1, 11, 34, 11, 52, 61, 1, 34]
def unique(arr):
    a = {arr[0]}
    for i in range(1,len(arr)):
        a.add(arr[i])
    b = list(a)
    print(b)
unique(list1)

# anagram
def ana(input1, input2):
    a = sorted(input1)
    b = sorted(input2)
    if a == b:
        return True
    else:
        return False
print(ana('dog', 'god'))
print(ana('green', 'fox'))

# Palindrome builder
def pal(str):
    a = ""
    for i in range(len(str)-1,-1,-1):
        a += str[i]
    return str+a
print(pal(""))

# Palindrome searcher


# sort
def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def advance_bubble(arr, reverse = False):
    if reverse == False:
        b = bubble(arr)
    elif reverse == True:
        a = bubble(arr)
        b = a[::-1]
    return b






