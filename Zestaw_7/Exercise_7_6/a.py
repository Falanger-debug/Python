def a():
    while True:
        for value in [0, 1]:
            yield value


iterator_a = a()
print([next(iterator_a) for _ in range(1000)])
