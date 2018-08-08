class stack_using_ll_with_header:

    class _Node(object):
        __slots__ = ("_val", "_next")
        def __init__(self, e, next):
            self._val = e
            self._next = next

    def __init__(self):
        self._header = _Node(None, None)
        self._n = 0
        self._top = self._header

    def push(self, e):
        new_node = _Node(e, self._top)
        self._top = new_node
        self._n += 1

    def is_empty(self):
        return self._size == 0

    def pop(self):
        if self.is_empty():
            raise EmptyException("Empty stack")
        temp = self._top
        self._top = self._top._next
        val = temp._val
        temp = None
        self._n -= 1
        return temp._val

    def __len__(self):
        return self._n
