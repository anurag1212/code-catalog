def dot(a, b):
    if len(a) != len(b):
        return "Bad values"
    return [a[i]*b[i] for i in range(len(a))]

print(dot([1,2,3],[4,5,6]))
