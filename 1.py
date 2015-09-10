# https://projecteuler.net/problem=1

def multiple(a, b):
    total = 0
    for i in range(a, b):
        if i % 3 == 0 or i % 5 == 0:
             total += i
    return total

print multiple(0, 1000)

