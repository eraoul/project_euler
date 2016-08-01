from timeit import timeit

x = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

import numpy as np

@timeit
def solution():
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
        print row, x
        val = triangle[row][x] + max(score_path(row+1,x), score_path(row+1,x+1))
        h[row][x] = val
        return val

    print score_path(0,0)

solution()