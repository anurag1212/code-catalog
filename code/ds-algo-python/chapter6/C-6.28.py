def enqueue(self, e):
    if self._size == self._maxlen:
        raise Full("Q is full")
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1
