def sortk(s, k, foi=None, lei=None):
    if foi is None or lei is None:
        foi = 0
        lei = len(s)-1
    while(foi<len(s) and s[foi]<k):
        foi += 1
    while(lei>=0 and s[lei]>=k):
        lei -= 1
    if foi > len(s)-1 or lei < 0 or foi > lei:
        return
    s[foi], s[lei] = s[lei], s[foi]
    sortk(s, k, foi, lei)

s=[1,4,3,5,1,2,4,6,8,9,0,12,3]
sortk(s,6)
print(s)
