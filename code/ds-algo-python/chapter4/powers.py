def power1(n,d):
    if d==0:
        return 1
    else:
        return n*power1(n,d-1)

def power2(n,d):
    if d==0:
        return 1
    else:
        if d%2==1:
            return n*power2(n,d//2)*power2(n,d//2)
        else:
            return power2(n,d//2)*power2(n,d//2)

def power3(n,d):
    if d==0:
        return 1
    else:
        partial = power3(n,d//2)
        if d%2==1:
            return n*partial*partial  # the n here is the problem solver
        else:
            return partial*partial

print(power1(4,4))
print(power2(4,4))
print(power3(4,4))
