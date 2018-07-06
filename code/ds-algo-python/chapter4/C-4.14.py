def hanoi(a,b,c):
    if isempty(c):
        return a
    else:
        b.push(pop(a))
        c.push(pop(b))
