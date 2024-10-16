big_number = 10000001231231231010


def number_of_zeros(number):
    number = str(number)
    count = 0
    for i in number:
        if i == "0":
            count += 1
    return count


print(number_of_zeros(big_number))
