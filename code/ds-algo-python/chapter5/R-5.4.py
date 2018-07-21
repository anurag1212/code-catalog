def __getitem__ (self, k):
    if not abs(k) < self._n:
        raise IndexError("invalid index")
    if k<0:
        return self._A[self._n-abs(k)]
    return self._A[k]
