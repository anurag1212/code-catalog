def transfer(S,T):
    temp = []
    while s:
        temp.append(s.pop())
    while T:
        S.append(T.pop())
    i = 0
    while i<len(temp):
        T.append(temp[i])
