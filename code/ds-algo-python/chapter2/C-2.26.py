class ReversedSequenceIterator:
    """
    Reversed Sequence Iterator
    """

    def __init__(self, data):
        self._data = data
        self._pos = len(self._data)

    def __next__(self):
        self._pos -= 1
        if self._pos < 0:
            raise StopIteration()
        else:
            return self._data[self._pos]

    def __iter__(self):
        return self


ri = iter(ReversedSequenceIterator([1,2,3]))
print(next(ri))
print(next(ri))
print(next(ri))
print(next(ri))
