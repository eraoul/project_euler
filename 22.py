from timeit import timeit

@timeit
def solution():
    f = open('p022_names.txt')
    names = sorted([t[1:-1] for t in f.read().split(',')])
    print names
    print len(names)

    s = 0
    for i, name in enumerate(names):
        score = sum(ord(c)-ord('A')+1 for c in name)
        s += (i+1)*score
    print s

solution()