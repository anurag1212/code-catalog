def max(self):
    f = self.first()
    max = f
    while self.after(f):
        f = self.after(f)
        max = max if max.element().value>f.element().value f
    return max.element()
