N = 1000

results = []
for i in xrange(1, N):
    if i % 3 == 0:
        results.append(i)
    elif i % 5 == 0:
        results.append(i)

print results
print sum(results)