def distinctpair(data):
    return(bool(len({i for i in data if i%2==1})-1))

print(distinctpair([2,5,6,8,5]))
