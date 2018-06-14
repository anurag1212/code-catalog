def __sub__(self, other):
    if len(self) != len(other):
        raise ValueError("Unequal lists")
    ans = Vector(len(self))
    ans._coords = [i-j for i,j in zip(self._coords, other._coords)]

# I wanted to use zip just cause
