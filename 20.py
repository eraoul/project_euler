
f = 1
for i in xrange(2, 101):
    f *= i
print f

sum = 0
while f > 0:
    sum += f % 10
    f /= 10

print sum