from timeit import timeit

@timeit
def solution():
    t = 0
    i = 1
    while True:
        t += i
        sqrt_t = t**0.5
        #print "triange(%d): %d" % (i, t)

        # compute divisors
        div = 2
        for j in xrange(2, int(sqrt_t)):
            if t%j==0:
                div += 2
                if j==sqrt_t:
                    div -=1
                if div > 500:
                    print t
                    return
        i += 1

solution()