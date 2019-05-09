# reversed admin
import re
str1, str2 = 'Admin', 'admin'
a = re.compile('[aA]dmin')
print(a.match(str1))
print(a.match(str2))

# number below 100
a = re.compile('^100|[0-9]?[0-9]$')
print(a.match('0'))
print(a.match('23'))
print(a.match('100'))
print(a.match('101'))

# Hungarian phone number
a = re.compile('00\s|\+36\s[\d]{2,2}\s[\d]{3,3}\s[\d]{4,4}')
print(a.match('+36 20 473 2746'))
print(a.match('00 36 70 381 1288'))
print(a.match('+36 20 3173 4717'))

# GFA email address
a = re.compile('(\w+)@greenfox\w+\.\w+')
cc = a.match('john@greenfoxacademy.com')
print(a.match('john@greenfoxacademy.com'))
print(a.match('john@wick.com'))
print(cc.groups())

# +1(000)123-1234 America phone number
a = re.compile('\+1\(\d\d\d\)\d\d\d-\d\d\d')
print(a.match('+36 20 473 2746'))
print(a.match('+1(000)123-1234'))

# image source
a = re.compile(r'\.?/?\w*/?\w*\-?\w*.png')
aa = a.search('<img src="dog.png">')
bb = a.search('<img alt="Cat picture" src="./images/cat-01.png">')
print(aa)
print(bb)
print(aa.group())
print(bb.group())
print(a.search('<script src="jquery.js"></script>'))

# RegexOne
a = re.compile('^\-?\d+(,\d+)*(\.\d+(e\d+)?)?$')
print(a.match('3.14529'))
print(a.match('1.2e10'))
