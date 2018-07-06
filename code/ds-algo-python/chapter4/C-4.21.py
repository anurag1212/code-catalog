def twosumsorted(s, k, foi=None, lei=None):
    if foi is None or lei is None:
        foi = 0
        lei = len(s)-1
    sum=s[foi]+s[lei]
    if sum==k:
        return (s[foi],s[lei])
    if(foi<len(s) and sum<k):
        foi += 1
    if(lei>=0 and sum>k):
        lei -= 1
    if foi > len(s)-1 or lei < 0 or foi > lei:
        return False
    return twosumsorted(s, k, foi, lei)

s=[1,2,5,6,8,9,11,14,18]
print(twosumsorted(s,23))
print(twosumsorted(s,22))
print(twosumsorted(s,21))
