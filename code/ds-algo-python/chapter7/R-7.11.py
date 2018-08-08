def max_pos(l):
    f = l.first()
    max = f
    while after(f):
        f = after(f)
        max = max if max.element().value>f.element().value f
    return max.element()
