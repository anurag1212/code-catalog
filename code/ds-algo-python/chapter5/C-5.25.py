def remove_all(l,val):
    firstNone = None
    for i in range(len(l)):
        if l[i]==val:
            l[i]=None
            if firstNone is None:
                firstNone = i
    print(l)
    i=firstNone
    j=i+1
    while i<len(l) and j<len(l):
        if l[j] is not None and l[i] is None:
            l[i],l[j] = l[j],l[i]
        if l[j] is None:
            j+=1
        if l[i] is not None:
            i+=1


l=[2,3,4,6,7,1,3,5,3,5,7,8]
print(l)
remove_all(l,3)
print(l)
