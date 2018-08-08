class rec_ll:
    class _Node(object):
        __slots__ = "_e","_next"
        def __init__(self):
            self._e = None
            self._next = None

    def __init__(self, e):
        self._head._e = e
        self._head._next = None
        self._tail = self

    def add(self,e):
        new = rec_ll(e)
        self._tail._next = new
        self._tail = self._tail._next
