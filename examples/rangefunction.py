def range(start, stop, step=1):
    i = 0
    while i < stop:
        yield i
        i += step
