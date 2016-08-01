from timeit import timeit

@timeit
def solution():
    sum_sq = sum([i*i for i in range(101)])
    sq_sum = sum(range(101))**2
    print sum_sq, sq_sum, sq_sum - sum_sq

solution()