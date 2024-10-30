line1 = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore "
    "magna aliqua.")


def longest_word_in_line(line):
    split = line.split()
    longest_word = max(split, key=len)
    print(f"Longest word in the line: {longest_word} with length: {len(longest_word)}")
    return ""


longest_word_in_line(line1)
