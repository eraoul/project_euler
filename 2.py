f = {0: 1, 1:1}

def fib(n):
    if n in f:
       return f[n]
    x = fib(n-2) + fib(n-1)
    f[n] = x
    return x

i = 1
s = 0
while True:
    x = fib(i)
    if x > 4000000:
        break
    if x % 2 == 0:
        print x
        s = s + x
    i = i + 1

print

print s

for i in xrange(4787):
    fib(i)
