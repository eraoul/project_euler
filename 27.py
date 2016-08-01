from timeit import timeit

@timeit
def solution():
    # Generate lots of primes
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
            primes.append(i)
        i += 1
        if i > 8000000:
            break
    print len(primes)
    print primes[-1]
    prime_set = frozenset(primes)

    max = -1
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            is_prime = True
            x = -1
            while is_prime:
                prev_x = x
                x = n*n + a*n + b
                is_prime = x in prime_set
                n += 1
            if n > max:
                max = n  # max is 1 too high, but it doesn't matter
                argmax = (a, b, prev_x)
                print max, argmax
    print max-1, argmax
    print argmax[0] * argmax[1]

solution()