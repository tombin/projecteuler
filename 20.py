def factorial(number):
    factorials = [ x for x in range(number, 0, -1) ]
    product = [ int(x) for x in str(reduce(lambda x, y: x * y, factorials)) ]
    return sum(product)

print factorial(100)                        
