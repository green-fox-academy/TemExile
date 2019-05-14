def writeoneline(name):
    try:
        text1 = open('my-file.txt', 'w')
        text1.write(name)
        text1.close()
    except OSError:
        print('Unable to write file: my-file.txt')
writeoneline('Haoxiang')

def writemoreline(path, word, number):
    try:
        text1 = open(path, 'a')
        for i in range(number):
            text1.write(word)
        text1.close()
    except OSError:
        print(f'Unable to write file: {path}')

writemoreline('multi-lines.txt', 'Haoxiang\n', 3)