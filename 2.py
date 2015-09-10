# https://projecteuler.net/problem=2

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

def getTotal(n):
    # n should be the fibonacci return value not to exceed
    total = 0
    fibValue = 0
    i = 0
    while(fibValue <= n):
        fibValue = fib(i+2)
        if fibValue % 2 == 0:
            total += fibValue
        i += 1
    return total

print getTotal(4000000)
