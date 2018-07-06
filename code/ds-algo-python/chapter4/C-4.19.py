def evenfirst(s, foi=None, lei=None):
    if foi is None or lei is None:
        foi = 0
        lei = len(s)-1
    while(foi<len(s) and s[foi]%2==0):
        foi += 1
    while(lei>=0 and s[lei]%2==1):
        lei -= 1
    if foi > len(s)-1 or lei < 0 or foi > lei:
        return
    s[foi], s[lei] = s[lei], s[foi]
    evenfirst(s, foi, lei)

s=[5,2,6,7,8,1,14,53,12,11,9,88,10]
s1=[4,1,5,2,9,11,23]
evenfirst(s)
print(s)
evenfirst(s1)
print(s1)
