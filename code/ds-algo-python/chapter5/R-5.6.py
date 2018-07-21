def insert(self, k, value):
    if self._n == self._capacity:
        self._B = [None]*2*self._capacity
    for j in range(self._n, k, −1):
        self._B[j] = self._A[j−1]
    self._B[k] = value
    for j in range(k-1, -1, −1):
        self._B[j] = self._A[j]
    self._A = self._B
    self._n += 1
