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


class RootProg(Progression):
    def __init__(self, start=65536):
        self._curr = start

    def _advance(self):
        self._curr = pow(self._curr, 1/2)

a = RootProg()
a.print_progression(50)
