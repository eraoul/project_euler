from timeit import timeit

k = 20
N = k + 1

@timeit
def solution():
    d = {(N, N): 1}
    for i in xrange(N, 0, -1):
        for j in xrange(N, 0, -1):
            if (i,j) in d:
                continue
            if i == N:
                d[(i,j)] = d[(N, j+1)]
                continue
            if j == N:
                d[(i,j)] = d[(i+1, N)]
                continue
            d[(i,j)] = d[(i+1, j)] + d[(i, j+1)]

    print d[(1,1)]

solution()