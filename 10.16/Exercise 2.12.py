line1 = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore "
    "magna aliqua.")


def string_of_the_first_letters(line):
    split = line.split()
    return "".join([word[0] for word in split])


def string_of_the_last_letters(line):
    split = line.split()
    return "".join([word[-1] for word in split])


print(string_of_the_first_letters(line1))
print(string_of_the_last_letters(line1))
