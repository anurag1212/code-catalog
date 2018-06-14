def __neg__(self):
    ans = Vector(len(self))
    for i in range(len(self)):
        ans[i] = -self[i]
    return ans
