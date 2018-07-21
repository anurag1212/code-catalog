def transfer(S,T):
    temp = []
    while S:
        temp.append(S.pop())
    while T:
        S.append(T.pop())
    i = 0
    for i in temp:
        T.append(i)

S,T,U = [1,2,3,4,5],[],[]
print(S)
transfer(S,T)
transfer(T,U)
transfer(U,S)
print(S)
