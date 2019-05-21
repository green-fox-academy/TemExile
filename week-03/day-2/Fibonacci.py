def fibonacci(num):
    if num <= 2 and num > 0:
        return [x for x in range(num)]
    elif num <= 0:
        return f'Please enter a valid index'
    else:
        start = [0,1]
        for i in range(2,num+1):
            start.insert(i, start[i-2]+start[i-1])
        return start
