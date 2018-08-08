def push(self, e):
    if self._n==self._capacity:
        t=self._top
        for _ in range(self._n-2):
            t=t._next
        rem=t._next
        rem=None
        t._next=None
        self._n-=1
    new=_Node(e)
    new.next = self._top
    self._top = new
    self._n+=1
