class stk_using_q:
    def __init__(self, capacity):
        self._q = [None]*capacity
        self._f = 0
        self._size = 0

    def push(self, e):
        self.enqueue(e);

    def pop(self):
        for i in range(0, self._size-1):
            self.enqueue(self.dequeue())
        self._dequeue()

    def top():
        for i in range(0, self._size-1):
            self.enqueue(self.dequeue())
        res = self._dequeue()
        print(res)
        self.enqueue(res)

# I assumed circular.
