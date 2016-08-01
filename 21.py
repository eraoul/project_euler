
from timeit import timeit

def proper_divisors(n):
    d = [1]
    for i in xrange(2, n/2 + 1):
        if n%i == 0:
            d.append(i)
    return d


@timeit
def solution():
    h = {}
    a = {}

    for i in xrange(1, 10000):
        if i not in a:
            # num1
            if i in h:
                val = h[i]
            else:
                val = sum(proper_divisors(i))
                h[i] = val

            # num2
            if val in h:
                b = h[val]
            else:
                b = sum(proper_divisors(val))
                h[val] = b
            if i == b and not i==val:
                a[i] = True
                if val < 10000:
                    a[val] = True
    for v in a:
        print v, h[v]
    print sum(a.keys())


solution()
