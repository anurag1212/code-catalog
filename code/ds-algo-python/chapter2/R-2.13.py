def __rmul__(self, factor):
    if not isinstance(factor, int):
        raise TypeError("Wrong length")
    ans = Vector(len(self))
    for i in range(len(self)):
        ans[i] = self[i]*factor
    return ans
