try:
    text1 = open('my-file.txt', 'r')
    allline = text1.readlines()
    for line in alline:
        print(line)
except:
    print('Unable to the file: my-file.txt')

# count the lines
try:
    textt = open('my-file.txt', 'r')
    alline = text1.readlines()
    return len(alline)
except:
    return 0
