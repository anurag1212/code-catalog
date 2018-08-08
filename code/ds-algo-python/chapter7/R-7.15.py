def __reversed__(self):
    f = self.first()
    while self.before(f):
        yield f
        f = self.before(f)
