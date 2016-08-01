from timeit import timeit

d = {2: 2}

def seq(n):
    if n in d:
        return d[n]
    if n%2 == 0:
        v = seq(n >> 1)
    else:
        v = seq(3*n + 1)
    d[n] = v + 1
    return v + 1

@timeit
def solution():
    max = 2
    argmax = 2
    for i in xrange(1, 1000000):
        v = seq(i)
        if v > max:
            max = v
            argmax = i
    print argmax, max

solution()