from timeit import timeit

EPSILON = 0.00000001

@timeit
def solution():
    results = []
    for a in xrange(11, 100):
        for b in xrange(11, 100):
            naive_num = a/10
            naive_den = b%10
            if naive_den == 0:
                continue
            if a%10 != b/10:
                continue
            if a == b:
                continue

            naive_frac = float(naive_num)/naive_den
            if abs(float(a)/b - naive_frac) < EPSILON:
                print "%d/%d = %f vs %f" % (a, b, naive_frac, float(a)/b)
                results.append(float(a)/b)
    p = 1
    for i in results:
        p *= i
    print "%f" % p

solution()