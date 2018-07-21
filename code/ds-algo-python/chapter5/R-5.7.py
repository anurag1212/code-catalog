def find_rep(list):
    n=len(list)
    return sum(list)-(n)*(n-1)/2

print(find_rep([1,2,3,4,5,6,7,7,8,9,10,11,12]))
