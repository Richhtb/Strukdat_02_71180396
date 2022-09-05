from time import time
import timeit

def fibonacci_iteratif (n):
    n1,n2 = 0,1
    for i in range(n):
        n1,n2 = n2,n1+n2
    return n1

def fibonacci_rekursif(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n + 2)


n = 100
start = timeit.default_timer()
fibonacci_iteratif(n) 
end = timeit.default_timer()
fibonacciLooped = end - start

start = timeit.default_timer()
fibonacci_rekursif(n)
end = timeit.default_timer()
fibonacciRecursive = end - start

for i in range(1,n):
    print("n= ", n,"iterative= ",fibonacciLooped,"detik",",","Recursive= ",fibonacciRecursive,"detik")
