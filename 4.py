from timeit import timeit

@timeit
def solution():
    max = 0

    for i in xrange(999,99,-1):
        for j in xrange(999,99,-1):
            x = i*j
            if x > max:
                str_x = str(x)
                r = str_x[::-1]
                if str_x == r:
                    max = x
    print max


solution()