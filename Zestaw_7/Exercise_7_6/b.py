import random


def random_direction_iterator():
    directions = ["N", "E", "S", "W"]
    while True:
        yield random.choice(directions)


iterator_b = random_direction_iterator()
print([next(iterator_b) for _ in range(1000)])
