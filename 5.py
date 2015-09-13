# https://projecteuler.net/problem=5

currentNumber = 20 
while(True):
    if all(currentNumber % i == 0 for i in range(1,21)):
        print currentNumber
        break
    else:
        currentNumber += 20 

