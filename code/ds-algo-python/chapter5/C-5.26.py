def find5rep(l):
    return((sum(l)-((len(l)-4)*(len(l)-3))/2)/4)

print(find5rep([1,2,3,3,5,4,3,3,3]))
