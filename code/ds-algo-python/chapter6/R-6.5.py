def stackrev(l):
    temp=[]
    while(l):
        temp.append(l.pop())
    while(temp):
        l.append(temp.pop())
