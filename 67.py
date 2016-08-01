from timeit import timeit
import numpy as np

@timeit
def solution():
    f = open('p067_triangle.txt')
    x = f.read()

    nums = [int(s) for s in x.replace('\n', ' ').strip().split(' ')]

    row_num = 0
    i = 0
    triangle = []
    while i < len(nums):
        row = []
        for j in xrange(row_num + 1):
            row.append(nums[i+j])
        triangle.append(row)
        row_num += 1
        i += row_num

    h = np.zeros((len(triangle), len(triangle)))

    def score_path(row, x):
        if h[row][x] > 0:
            return h[row][x]
        if row==len(triangle)-1:
            return triangle[row][x]
        val = triangle[row][x] + max(score_path(row+1,x), score_path(row+1,x+1))
        h[row][x] = val
        return val

    print score_path(0,0)

solution()