from timeit import timeit

@timeit
def solution():
    # Generate primes
    primes = []
    i = 2
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
        if len(primes) == 10001:
            print primes[-1]
            break
        i += 1

@timeit
def solution2():
    # Generate primes
    primes = []
    i = 2
    while True:
        for p in primes:
            if i % p == 0:
                break
        else:
            #print i
            primes.append(i)

        if len(primes) == 10001:
            print primes[-1]
            break
        i += 1


solution()

solution2()
