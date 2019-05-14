try:
    text1 = open('my-file.txt', 'r')
    allline = text1.readlines()
    for line in alline:
        print(line)
except:
    print('Unable to the file: my-file.txt')