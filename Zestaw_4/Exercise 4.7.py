def flatten(sequence):
    if isinstance(sequence, (list, tuple)):
        return [item for sublist in sequence for item in flatten(sublist)]
    return [sequence]


assert (flatten([1, 2, 3, [4, 5, [1, [10, []]]], (6, 7)]) == [1, 2, 3, 4, 5, 1, 10, 6, 7])
