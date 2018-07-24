class deq_using_2_stks:
    def self.__init__(self, capacity):
        self._s1 = [None]*capacity
        self._s1 = [None]*capacity

    def enqueue_front(self, e):
        self._s1.push(e)

    def enqueue_last(self, e):
        self._s2.push(e)

    def dequeue_front(self):
        if self._s2:
            return self._s2.pop()
        else:
            for _ in range(0,len(self._s1)-1):
                self._s2.push(self._s1.pop())
            return self._s1.pop()

    def dequeue_last(self):
        if self._s1:
            return self._s1.pop()
        else:
            for _ in range(0,len(self._s2)-1):
                self._s1.push(self._s2.pop())
            return self._s2.pop()
