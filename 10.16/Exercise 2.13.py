word1 = """A bacon ipsum dolor amet kevin turducken short a loin porchetta pork chop, shank cow frankfurter landjaeger 
ground round pastrami. """
word2 = "d"
word3 = "d a"
word4 = ""


def complete_length_of_words(word):
    split = word.split()
    if not split:
        return 0
    return sum([len(word) for word in split])


print(complete_length_of_words(word1))
print(complete_length_of_words(word2))
print(complete_length_of_words(word3))
print(complete_length_of_words(word4))





