# simple replace
example = "In a dishwasher far far away"
example = example.split()
example[2] = "galaxy"
example = ' '.join(example)
print(example)

# url fixer
url = "https//www.reddit.com/r/nevertellmethebots"
url1 = "https:"
url2 = "odds"
url = url[5:-4]
url = url1 + url + url2
print(url)

# take longer
quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
quote1 = quote[:21]
quote2 = quote[20:]
quote3 = "always takes longer than"
quote = quote1 + quote3 + quote2
print(quote)

# to do print
todoText = " - Buy milk\n"
quote1 = "My todo:\n"
quote3 = " - Download games\n"
quote4 = "     - Diablo"
todoText = quote1 + todoText + quote3 + quote4
print(todoText)

# reverse
reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
def reverse(str):
    a = ""
    for i in range(len(str)):
        a = str[i] + a
    return a
print(reverse(reversed))

# list introduction 1
alist = []
print(len(alist))
alist.append("William")
print(alist == [])
alist.append("John")
alist.append("Amanda")
print(len(alist))
print(alist[2])
for i in range(len(alist)):
    print(alist[i])
for i in range(len(alist)):
    print(str(i+1)+". "+str(alist[i]))
alist.remove(alist[1])
for i in range(len(alist)-1,-1,-1):
    print(alist[i])
alist = []

# Map introducation 1
amap = {}
print(amap == {})
amap.update({"97":"a", "98":"b", "99":"c", "65":"A", "66":"B","67":"C" })
print(amap.keys())
print(amap.values())
amap["68"] = "D"
print(len(amap))
print(amap["99"])
amap.pop("97")
print("100" in amap)
amap = {}

# list introduction 2
lista = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
listb = lista
print('Durian' in lista)
listb.remove('Durian')
lista.insert(4,"Kiwifruit")
lista.index("Avocado")
listb.index("Durian")
listb.extend(["Passion Fruit", "Pummelo"])
print(lista[2])

# map introduction 2
bk = {'978-1-60309-452-8':'A Letter to Jo', '978-1-60309-459-7':'Lupus', '978-1-60309-444-3':'Red Panda and Moon Bear',
      '978-1-60309-461-0': 'The Lab'}
for i in range(len(bk)):
    key, value = list(bk.keys()), list(bk.values())
    print(f"{value[i]} (ISBN: {key[i]})")
bk.pop('978-1-60309-444-3')
def delfromvalue(dict1, value):
    a = list(dict1.values())
    c = a.index(value)
    b = list(dict1.keys())
    dict1.pop(b[c])
    return dict1
delfromvalue(bk, 'The Lab')
bk.update({'978-1-60309-450-4':'They Called Us Enemy','978-1-60309-453-5':'Why Did We Trust Him?'})
print('478-0-61159-424-8' in bk)
print(bk['978-1-60309-453-5'])

# personal finance
flist = [500, 1000, 1250, 175, 800, 120]
def totalspend(arr):
    print(sum(arr))
def grestestspend(arr):
    print(max(arr))
def cheapestspend(arr):
    print(min(arr))
def avespend(arr):
    print(round(sum(arr)/len(arr),2))

# telephone book
teledict = {'William A. Lathan':'405-709-1865', 'John K. Miller':'402-247-8568',
            'Hortensia E. Foster':'606-481-6467', 'Amanda D. Newland':'319-243-5613',
            'Brooke P. Askew':'307-687-2982'}
def findphone(arr,ppl):
    print(arr[ppl])
def findpeople(dict1,value):
    a = list(dict1.values())
    c = a.index(value)
    b = list(dict1.keys())
    print(b[c])
print('Chris E. Myers' in teledict)

# shopping list
slist = ['Egg','milk','fish','apples','bread','chicken']
def knowtheitem(arr, items):
    print(items in slist)

# Product database
pmap = {'egg':200, 'milk':200, 'fish':400, 'apples':150, 'bread':50, 'chicken':550}
print(pmap['fish'])
def findthemax(map):
    a = list(map.values())
    b = max(a)
    c = a.index(b)
    d = list(map.keys())
    print(d[c])
def findtheave(map):
    a = list(map.values())
    print(round(sum(a)/len(a),2))
def countnum(map):
    a = list(map.values())
    b = []
    for i in range(len(a)):
        if a[i] <= 300:
            b.append(a[i])
    print(len(b))
print(125 in pmap.values())
def findthemin(map):
    a = list(map.values())
    b = min(a)
    c = a.index(b)
    d = list(map.keys())
    print(d[c])

# Product database 2
pmap = {'egg':200, 'milk':200, 'fish':400, 'apples':150, 'bread':50, 'chicken':550}
def findless(map, value):
    a = list(map.values())
    b = list(map.keys())
    for i in range(len(a)):
        if a[i] < value:
            print(b[i])
def findmore(map, value):
    a = list(map.values())
    b = list(map.keys())
    for i in range(len(a)):
        if a[i] > value:
            print(f'{b[i]} + {a[i]}')

# shopping list 2


product = {'milk':1.07, 'rice':1.59, 'eggs':3.14, 'cheese':12.60, 'chicken breasts':9.40,
           'apples':2.31,'tomato':2.58,'potato':1.75,'onion':1.1}
bob = {'milk':3, 'rice':2, 'eggs':2, 'cheese':1, 'chicken breasts':4,
       'apples':1, 'tomato':2, 'potato':1}
alice = {'rice':1, 'eggs':5, 'chicken breasts':2, 'apples':1, 'tomato':10}
def totalpay(map):
    product = {'milk': 1.07, 'rice': 1.59, 'eggs': 3.14, 'cheese': 12.60, 'chicken breasts': 9.40,
               'apples': 2.31, 'tomato': 2.58, 'potato': 1.75, 'onion': 1.1}
    maplist = list(map.keys())
    price = []
    for i in range(len(maplist)):
        p1 = product.get(maplist[i])
        p2 = map.get(maplist[i])
        p2 = float(p2)
        p3 = p1 * p2
        price.append(p3)
    print(sum(price))
def buymore(pro):
    bob = {'milk': 3, 'rice': 2, 'eggs': 2, 'cheese': 1, 'chicken breasts': 4,
           'apples': 1, 'tomato': 2, 'potato': 1}
    alice = {'rice': 1, 'eggs': 5, 'chicken breasts': 2, 'apples': 1, 'tomato': 10}
    if (pro in bob) and (pro in alice):
        if alice.get(pro) > bob.get(pro):
            print('Alice buy more '+pro)
        elif alice.get(pro) < bob.get(pro):
            print('Bob buy more '+pro)
        else:
            print('They buy the same amount of '+pro)
    elif not(pro in bob):
        print('Alice buy more '+pro)
    elif not(pro in alice):
        print('Bob buy more ' + pro)
buymore('rice')
buymore('potato')
def moretype():
    bob = {'milk': 3, 'rice': 2, 'eggs': 2, 'cheese': 1, 'chicken breasts': 4,
           'apples': 1, 'tomato': 2, 'potato': 1}
    alice = {'rice': 1, 'eggs': 5, 'chicken breasts': 2, 'apples': 1, 'tomato': 10}
    if len(bob) > len(alice):
        print("Bob buy more different products")
    elif len(bob) < len(alice):
        print("Alice buy more different products")
    else:
        print("They buy the same")
def morepices():
    bob = {'milk': 3, 'rice': 2, 'eggs': 2, 'cheese': 1, 'chicken breasts': 4,
           'apples': 1, 'tomato': 2, 'potato': 1}
    alice = {'rice': 1, 'eggs': 5, 'chicken breasts': 2, 'apples': 1, 'tomato': 10}
    blist = list(bob.values())
    alist = list(alice.values())
    bsum = sum(blist)
    asum = sum(alist)
    if bsum > asum:
        print("Bob buy more pieces")
    elif bsum < asum:
        print("Alice buy more pieces")
    else:
        print("They buy the same")

# solar system
planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
def put_saturn(arr):
    arr.append("Saturn")
    temp = arr[5:]
    arr[5:] = temp[2], temp[0], temp[1]
    return arr
print(put_saturn(planet_list))

# matchmaking
def making_matches(arr1, arr2):
    b = min(len(arr1), len(arr2))
    a = []
    for i in range(b):
        a.append(arr1[i])
        a.append(arr2[i])
    a1 = arr1[b:]
    a2 = arr2[b:]
    if len(arr1) != b:
        a = a+a1
    elif len(arr2) != b:
        a = a+a2
    return a
girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]
print(making_matches(girls, boys))

# append letter
def create_new_verbs(a, b):
    c = []
    for i in range(len(b)):
        d = a + b[i]
        c.append(d)
    return c
verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"
print(create_new_verbs(preverb, verbs))

#candy shop
shop_items = ["Cupcake", 2, "Brownie", False]
def sweets():
    a = shop_items.index(2)
    b = shop_items.index(False)
    shop_items[a], shop_items[b] = "Croissant" , "Ice cream"
    return shop_items
print(sweets())

# element finder
numbers = [1, 2, 3, 4, 5, 6, 8]
def contains_seven(num):
    if 7 in num:
        return "Hoorray"
    else:
        return "Noooooo"
print(contains_seven(numbers))

# is_in_list
list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
def check_nums(arr):
    check = [4,8,12,16]
    ar = []
    for i in range(len(check)):
        if check[i] in arr:
            a = True
        else:
            a = False
        ar.append(a)
    if sum(ar) == len(check):
        return True
    else:
        return False
print(check_nums(list_of_numbers))

# quote swap
words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]
def quote_swap(arr):
    temp = arr[2], arr[5]
    arr[5], arr[2] = temp
    a = arr[0]
    for i in range(1, len(words)):
        a = a+" "+arr[i]
    return a
print(quote_swap(words))

# calculator
## still working on it

# he will never
out = "";
not_so_cryptic_message = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11]
hashmap = {

    7: "run around and desert you",

    50: "tell a lie and hurt you ",

    49: "make you cry, ",

    2: "let you down",

    12: "give you up, ",

    1: "Never gonna ",

    11: "\n",

    3: "say goodbye "

}
for i in range(len(not_so_cryptic_message)):
    out = out+" "+hashmap[not_so_cryptic_message[i]]
print(out)



