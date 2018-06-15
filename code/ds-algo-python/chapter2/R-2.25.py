def __mul__(self, other):
    ans = Vector(len(self))
    if isinstance(other, int):
        for i in range(len(self)):
            ans[i] = self[i]*other
    elif isinstance(factor, Vector):
        for i in range(len(self)):
            ans[i] = self[i]*other[i]
    else:
        raise TypeError("Bad Values")
    return ans
