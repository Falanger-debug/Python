line1 = ("Lorem ipsum GvR dolor sit amet, consectetur adipiscing elit. "
         "Sed do eiusmod tempor incididunt ut labore et ")


def sort_words_alphabetically(line):
    split = line.split()
    return sorted(split, key=lambda word: word.lower())
    # użyłem lambda zamiast str.lower() bo IDE podkreślało,
    # że nie wie czy lower() działa na całej liście czy na każdym
    # elemencie osobno

    # because of the warning I had to use lambda instead of str.lower()
    # now IDE is happy, cause it knows for sure that lower() is working of every word
    # individually and not just on the whole list


def sort_words_by_length(line):
    split = line.split()
    return sorted(split, key=len)


print(sort_words_alphabetically(line1))
print(sort_words_by_length(line1))
