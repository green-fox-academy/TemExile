try:
    text1 = open('my-file.txt', 'r')
    allline = text1.readlines()
    for line in alline:
        print(line)
except:
    print('Unable to the file: my-file.txt')

# count the lines
def countline(filename):
    try:
        textt = open(filename, 'r')
        alline = text1.readlines()
        return len(alline)
    except:
        return 0

countline('my-file.txt')