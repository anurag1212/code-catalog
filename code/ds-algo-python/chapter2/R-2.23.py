def __lt__(self, other):
    if len(self) != len(other):
        raise ValueError()
    for j in range(len(self)):
        if self[j] >= other[j]:
            return False
    return True
