from timeit import timeit

@timeit
def solution():
    i = 1
    divisors = range(20, 10, -1)
    while True:
        found = True
        for d in divisors:
            if i % d > 0:
                found = False
                break
        if found:
            print "Answer:", i
            break
        if i % 1000 == 0:
            print i
        i += 1


solution()


# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# 11, 12, 13, 14, 15, 16, 17, 18, 19, 20