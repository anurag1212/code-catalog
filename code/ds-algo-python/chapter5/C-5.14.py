from random import randrange
def my_shuffle(l):
    n=len(l)
    for i in range(n-1,0,-1):
        j=randrange(i+1)
        l[i], l[j] = l[j], l[i]

l=[5,1,4,2,3,6,8]
print(l)
my_shuffle(l)
print(l)
