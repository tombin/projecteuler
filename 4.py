# https://projecteuler.net/problem=4

def isPal(number):
     number = str(number)
     if number == number[::-1]:
         return True
     else:
         return False

def getLargest(a, b):
    largest = []
    for x in range(a, b):
        for y in range(a, b):
            results = x * y
            if isPal(results):
                largest.append(results)
    return max(largest)

print getLargest(100,1000)








