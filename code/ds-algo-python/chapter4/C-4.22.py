# 1 def power(x, n):
# 2 ”””Compute the value x n for integer n.”””
# 3 if n == 0:
# 4 return 1
# 5 else:
# 6 partial = power(x, n // 2) # rely on truncated division
# 7 result = partial partial
# 8 if n % 2 == 1: # if n odd, include extra factor of x
# 9 result *= x
# 10 return result

def pow_iter(n,d):
    result=1
    s=[]
    while(d>0):
        if d%2 == 1:
            s.append(n)
        else:
            s.append(result)
        d//=2
    for i in reversed(s):
        result=result*result*i
    return result

print(pow_iter(5,5))
print(pow_iter(3,6))
print(pow_iter(2,0))
