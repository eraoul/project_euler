

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def pf(n):
    # # Generate primes up to sqrt(n)
    # primes = []
    # for i in xrange(2, int(n**0.5) + 1):
    #     prime = True
    #     for p in primes:
    #         if i % p == 0:
    #             prime = False
    #             break
    #     if prime:
    #         print i
    #         primes.append(i)

    # find largest prime factor of n
    # for p in reversed(primes):
    #     if n % p == 0:
    #         return p

    for i in xrange(2, n/2 + 1):
        if n % i == 0:
            result = n/i
            if isPrime(result):
                return result

print pf(127)
print pf(13195)
print pf(600851475143)  # returns 6857