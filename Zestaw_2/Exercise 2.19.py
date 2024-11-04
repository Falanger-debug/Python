L = [23, 89, 125, 75, 1, 2, 399, 8]


def create_string_of_3_digits_numbers(list_of_numbers):
    return "".join([str(i).zfill(3) for i in list_of_numbers])


print(create_string_of_3_digits_numbers(L))
