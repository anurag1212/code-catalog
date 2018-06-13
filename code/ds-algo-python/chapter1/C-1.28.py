def norm(v, p=2):
    a=(sum([pow(i,p) for i in v]))
    print(pow(a,p))
    print(pow(a,p*-1))
    return pow(sum([pow(i,p) for i in v]),p*-1)

print(norm([3,4],2))
