word1 = """A bacon ipsum dolor amet kevin turducken short a loin porchetta pork chop, shank cow frankfurter landjaeger 
ground round pastrami. """
word2 = "d"
word3 = "d a"
word4 = ""


def print_with_underscore(word):
    split = word.split()
    if not split:
        return
    print("_".join(split))


print_with_underscore(word1)
print_with_underscore(word2)
print_with_underscore(word3)
print_with_underscore(word4)
