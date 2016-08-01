from timeit import timeit

N = 1000

@timeit
def solution1():
    x = 1 << N
    print x
    s = 0
    while x > 0:
        s += x%10
        x /= 10
    print s

@timeit
def solution2():
    x = 1 << N
    print sum(int(c) for c in str(x))

solution1()
solution2()