def factors(n): # generator that computes factors
    k = 1
    temp = []
    while k*k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            temp.append(n // k)
        k += 1
    if k*k == n: # special case if n is perfect square
        yield k
    for i in reversed(temp):
        yield i

print([i for i in factors(15)])
