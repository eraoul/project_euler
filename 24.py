from timeit import timeit

@timeit
def solution():
    a = [0,1,2,3,4,5,6,7,8,9]

    bkwd_rng = range(8, -1, -1)

    for i in xrange(1000000-1):
        # Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
        for k in bkwd_rng:
            if a[k] < a[k+1]:
                break

        # Find the largest index l greater than k such that a[k] < a[l].
        for l in xrange(9, k, -1):
            if a[k] < a[l]:
                break

        # Swap the value of a[k] with that of a[l].
        a[k], a[l] = a[l], a[k]

        # Reverse the sequence from a[k + 1] up to and including the final element a[n].
        a[k+1:] = reversed(a[k+1:])

    print ''.join(str(x) for x in a)

solution()

