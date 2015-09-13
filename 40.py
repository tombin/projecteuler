# https://projecteuler.net/problem=40

def genNumber(max):
    number = ''.join([str(i) for i in range(0, max)])
    return number

def getProduct(number, max): 
    total = 1
    counter = 0
    while(10 ** counter <= max):
       total *= int(number[10 ** counter])
       counter += 1
    return total

max = 1000000
print getProduct(genNumber(max), max) 



