from timeit import timeit

def sum_proper_divisors(n):
    d = 1
    for i in xrange(2, n/2 + 1):
        if n%i == 0:
            d += i
    return d

@timeit
def solution():
    abundant = []
    a_hash = {}
    for i in xrange(12, 28124):
        if sum_proper_divisors(i) > i:
            abundant.append(i)
            a_hash[i] = True

    sum = 0
    for i in xrange(1, 28124):
        for a in abundant:
            if a_hash.get(i-a):
                break
        else:
            sum += i
    print sum

solution()
