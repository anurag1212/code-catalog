class q_using_2_stks:
    def __init__(self, capacity):
        self._s1 = [None]*capacity
        self._s2 = [None]*capacity

    def enqueue(self, e):
        self._s1.push(e);

    def dequeue(self):
        if self._s2:
            return self._s2.pop()
        else:
            for _ in range(0,len(self._s1)-1):
                self._s2.push(self._s1.pop())
            return self._s1.pop()

    def first(self):
        if not self._s2:
            for _ in range(0,len(self._s1)):
                self._s2.push(self._s1.pop())
         return self._s2[-1]
