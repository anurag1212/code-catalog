def recursive_max(S, curr=0, max=float('-inf')):
    if curr==len(S):
        return max
    return recursive_max(S, curr+1, S[curr] if S[curr]>max else max)

print(recursive_max([1,5,3,2,4]))
