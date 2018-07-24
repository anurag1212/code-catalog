def rotate(self):
    if self._size == 0:
        raise Empty()
    res = self._data[self._front]
    self._data[self._front] = None
    self._data[(self._front + self._size) % len(self._data)] = res
    self._front += 1
