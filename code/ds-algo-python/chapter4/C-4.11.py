def element_uniqueness(S,i=0,j=1):
    if j>=len(S):
        return True
    else:
        if S[i]==S[j]:
            return False
        else:
            sub_stack = True and element_uniqueness(S,i,j+1)
        return sub_stack if not sub_stack else sub_stack and element_uniqueness(S,i+1,i+2)

print(element_uniqueness([5,4,2,3,1,15,3]))
print(element_uniqueness([4,4]))
print(element_uniqueness([1]))
print(element_uniqueness([]))
