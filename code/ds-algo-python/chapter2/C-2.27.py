def __contains__(self, k):
    return ((k - self._start)%self._step == 0)
