from timeit import timeit

words_unit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
words_below_twenty = list(words_unit)
words_below_twenty.extend(['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'])
word_hundred = 'hundred'

len_units = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]
len_tens = [4, 3, 6, 6, 5, 5, 5, 7, 6, 6]
len_below_twenty = list(len_units)
len_below_twenty.extend([3, 6, 6, 8, 8, 7, 7, 9, 8, 8])

def int_to_word(n):
    if n==1000:
        return "one thousand"
    if n==0:
        return "zero"
    s = ''
    if n > 99:
        d = n/100
        s += words_unit[d]
        s += ' hundred'
        n -= d * 100
        if n > 0:
            s += ' and '
    if n > 19:
        d = n / 10
        s += words_tens[d]
        n -= d*10
        if n>0:
            s += ' '
            s += words_unit[n]
    elif n > 0:
        s += words_below_twenty[n]
    return s


def int_to_len(n):
    if n==1000:
        return 11 # "onethousand"
    if n==0:
        return 4 # "zero"
    s = 0
    if n > 99:
        d = n/100
        s += len_units[d]
        s += 7 # 'hundred'
        n -= d * 100
        if n > 0:
            s += 3 # 'and'
    if n > 19:
        d = n / 10
        s += len_tens[d]
        n -= d*10
        if n>0:
            s += len_units[n]
    elif n > 0:
        s += len_below_twenty[n]
    return s

@timeit
def solution1(N):
    s = 0
    for i in xrange(1, N+1):
        w = int_to_word(i)
        #print w
        s += len(w.replace(' ', ''))
    print s
    return s


@timeit
def solution2(N):
    s = sum(int_to_len(i) for i in xrange(1, N+1))
    print s
    return s

s1 = solution1(1000)  # should be 21124
print s1 == 21124

s2 = solution2(1000)  # should be 21124
print s2 == 21124
