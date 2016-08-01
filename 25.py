f = {1: 1, 2:1}

import math


def fib(n):
    if n in f:
       return f[n]
    x = fib(n-2) + fib(n-1)
    f[n] = x
    return x

i = 1
limit = 10**999
while True:
    x = fib(i)
    if x >= limit:
        break
    i += 1

print i
print x
