import itertools


def week_days_iterator():
    return itertools.cycle(range(7))


iterator_c = week_days_iterator()
print([next(iterator_c) for _ in range(1000)])
