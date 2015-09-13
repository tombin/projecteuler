def fib(number):
    fibList = [0, 1, 1]
    while(True):
        fibList.append(fibList[-1] + fibList[-2]) 
        if len(str(fibList[-1])) == number:
            return len(fibList) - 1
            break

print fib(1000)
