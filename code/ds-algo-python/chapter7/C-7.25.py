class q_using_ll_with_header:

    class _Node(object):
        __slots__ = ("_val", "_next")
        def __init__(self, e, next):
            self._val = e
            self._next = next

    def __init__(self):
        self._header = _Node(None, None)
        self._n = 0
        self._tail = self._header

    def __len__(self):
        return self._n

    def enqueue(self, e):
        self._tail._next = Node(e, None)
        self._tail = self._tail._next
        self._n += 1

    def is_empty(self):
        return self._size == 0

    def dequeue(self):
        if is_empty(self):
            raise EmptyException("Empty")
        temp = self._header._next
        self._header._next = temp._next
        retval = temp._val
        temp = None
        return retval
