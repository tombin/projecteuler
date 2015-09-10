# https://projecteuler.net/problem=3

def primes(number):
    results = []
    base = 2
    while base * base <= number:
        while number > 1:
            while number % base == 0:
                results.append(base)
                number = number / base 
            base += 1
    return results 

print "largest value: %d" % max(primes(10))
