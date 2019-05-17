def timetosec(str):
    a = str.split(':')
    total = 3600 * float(a[0]) + 60 * float(a[1]) + float(a[2])
    return total

def sectotime(num):
    sec = num % 60
    a = num // 60
    m = a % 60
    h = a // 60
    return str(h)+':'+str(m)+':'+str(sec)