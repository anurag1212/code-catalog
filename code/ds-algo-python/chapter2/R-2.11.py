def __radd__(self, other):
    if len(self) != len(other):
        raise ValueError("Wrong length")
    ans = Vector(len(self))
    for i in range(len(self)):
        ans[i] = other[i] + self[i]
    return ans
