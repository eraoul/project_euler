from timeit import timeit

@timeit
def solution():
    count = 0
    for i in xrange(10000):
        cur = i
        s = str(cur)
        rs = s[::-1]
        added = cur + int(rs)
        for j in xrange(49):
            s = str(added)
            rs = s[::-1]
            if (s==rs):
                #print 'palindrome from', i, 'in iters=', j
                break
            added = added + int(rs)
        else:
            #print "Lychrel:", i
            count += 1

    print count

solution()