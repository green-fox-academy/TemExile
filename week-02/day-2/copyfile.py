def copyfile(file1, file2):
    try:
        a = open(file1, 'r')
        content = a.read()
        a.close()
        b = open(file2, 'w')
        b.write(content)
        b.close()
        return True
    except OSError:
        return False

copyfile('copy1.txt', 'copy2.txt')