def find_min_max(S, n=None, min=float('inf'), max=float('-inf')):
    if n==None:
        n=len(S)-1
    if n<0:
        return (min,max)
    else:
        return find_min_max(S, n-1,
                            min if min<S[n] else S[n],
                            max if max>S[n] else S[n])

print(find_min_max([5,2,3,7,1,2,9,12,4]))
