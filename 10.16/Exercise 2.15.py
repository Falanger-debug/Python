L = [1331, 12, 12, 21, 12, 21, 121, 213, 1313, 1, 141, 211231, 1231]


def concatenate(list_of_numbers):
    return "".join([str(i) for i in list_of_numbers])


print(concatenate(L))
