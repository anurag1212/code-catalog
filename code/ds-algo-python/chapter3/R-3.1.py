import timeit
def dis(a,b,c):
    i=j=k=0
    while(i<len(a) or j<len(b) or k<len(c)):
        print("A:",a[i])
        while(j<len(b) and b[j]<a[i]):
            print("B:",b[j])
            while(k<len(c) and c[k]<b[j]):
                print("C:",c[k])
                if c[k]==b[j] and b[j]==a[i]:
                    return False
                k+=1
            if j<len(b)-1:
                j+=1
        if i<len(a)-1:
            i+=1
        if i==len(a)-1 and j==len(b)-1 and k==len(c)-1:
            return True
    return True

def dis2(a,b,c):
    i=j=k=0
    while(i<len(a)):
        while(b[j]<a[i]):
            j+=1
        while(c[k]<a[i]):
            k+=1
        if a[i]==b[j] and b[j]==c[k]:
            return False
        i+=1
    return True

# print(dis([1,2,3],[2,3,4],[3,4,5]))
print(dis2([1,2,3],[1,2,3],[3,4,4]))

"""
Lesson learnt. 45min wrong vs 45secs right. The difference was
being unbiased about symmetry/beauty of solution and simply
translating ideas into code; It wont always be this easy
"""
