def fizzbuzz(n):
    for _ in range(1,n+1):
        if _ % 3 == 0:
            yield 'fizz'
        elif _ % 5 == 0:
            yield 'buzz'
        elif _ % 3 == 0 and _ % 5 == 0:
            yield 'fizzbuzz'
        else:
            yield _

a = fizzbuzz(10)
