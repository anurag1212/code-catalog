def __pop__(self):
    if self._n>0:
        self._A[-1] = None
        self._n -= 1
    if (self._n-1)//4 >= self._capacity:
        self._resize(self._capacity//2)
