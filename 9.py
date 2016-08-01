from timeit import timeit

@timeit
def solution():
    for a in xrange(1, 333):
        for b in xrange(a, 1001):
            c = 1000-a-b
            if a*a + b*b == c*c:
                print a,b,c
                print a*b*c
                return
    print 'FAIL'

solution()