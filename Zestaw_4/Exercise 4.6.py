def sum_seq(sequence):
    if isinstance(sequence, (list, tuple)):
        return sum([sum_seq(item) for item in sequence])
    return sequence


assert ((sum_seq([1, 2, 3, [4, 5, [1, [10, []]]], (6, 7)])) == 39)
