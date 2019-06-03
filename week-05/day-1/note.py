# side effect
a = 0

def increment(amount):
    global a
    a = a + 1
    print(a)

increment(1)

def pure_increment(input_value, amount):
    return input_value + amount

# make data structure not changable
from collections import namedtuple

Person = namedtuple('Person', 'name age')
p1 = Person(name = 'John', age = 10)
print(p1)
# p2 = Person(mae = 'Tim', age = 25) will show a error since not such key
# p1.name = 'Bob' will have error since the value cannot be changed
