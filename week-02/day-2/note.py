# error-handing
drink = [
    'cola',
    'water'
]
# print(drink[3])
#index = input('Which item would you like to get?')
#print(drink[index])
index = int(input('Which item would you like to get?'))
print(drink[index])

# try, except, finally function
try:
    index = int(input('Which item would you like to get?'))
    print(drink[index])
except IndexError:
    print('please provide a valid index.')
except ValueError:
    print('please use the index instead of the name.')
finally:
    print('This will always run.')
print('Will it run?')

#raise function
def add(a,b):
    if isinstance(a, int) and isintaance(6, int):
        return a + b
    raise TypeError
try:
    print(add('4','3'))
except TypeError:
    print('you must wrote  integers')

class MyError(Exception):
    def __init__(self):
        super().__inti__()

# file application, file-manipulation
f = open()
content = f.readlines()
f.close()

print(type(content))
print(content)
print(len(content))

for line in content:
    print(line, end = '')

# write to file
f = open('aaa', 'r')
f.write('hello')

# append write
f = open('aaa', 'a')
f.write('hello\n')

# don't have to close the file with 'with' statement
with open('aaa', 'a') as f:
    f.write('aaaaaa')