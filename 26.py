from timeit import timeit

def cycle_len(N):
    iter = 0
    rem = 1
    rem_seen = {1:0}  # remainder, iteration number
    while True:
        while rem < N:
            iter += 1
            rem *= 10
        d = rem/N
        rem -= d*N
        if rem in rem_seen:
            length = iter - rem_seen[rem]
            break
        if rem==0:
            length = 0
            break
        rem_seen[rem] = iter
    return length

@timeit
def solution():
    max = 0
    for i in range(1, 1000):
        l = cycle_len(i)
        if l > max:
            max = l
            argmax = i
        print i, l, str(1.0/i)
    print "best:", argmax
    print "len:", max

solution()