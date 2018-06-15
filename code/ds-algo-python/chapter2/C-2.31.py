class Progression:
    def __init__(self, start=0):
        self._curr = start

    def _advance(self):
        self._curr += 1

    def __next__(self):
        if self._curr is None:
            raise StopIteration()
        else:
            answer = self._curr
            self._advance( )
        return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class DiffProg(Progression):
    def __init__(self, first=2, second=200):
        self._curr = first
        self._prev = first - second

    def _advance(self):
        self._curr, self._prev = abs(self._curr - self._prev), self._curr
        if self._curr == self._prev == 0:
            self._curr = None

a = DiffProg()
a.print_progression(50)
