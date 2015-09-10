# https://projecteuler.net/problem=6

def sqrt(num):
    return num**2

def sqsum(_range):
    total = 0
    for i in range(1, _range+1):
        total += 1
    return sqrt(total)


def squares(_range):
    total = 0
    for i in range(1, _range+1):
        total += sqrt(i)
    return total

_range = 100
print sqsum(_range) - squares(_range)
