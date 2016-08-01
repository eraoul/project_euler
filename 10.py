from timeit import timeit

@timeit
def solution():
    # Generate primes
    primes = []
    i = 2
    s = 0
    while True:
        prime = True
        for p in primes:
            if p*p > i:
                break
            if i % p == 0:
                prime = False
                break
        if prime:
            #print i
            primes.append(i)
            s += i
        i += 1
        if i > 2000000:
            break
    print s
solution()