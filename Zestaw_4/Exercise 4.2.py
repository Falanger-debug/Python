import sys


def make_ruler(length):
    if type(length) != int:
        raise ValueError("Input must be an integer")
    ruler = "|"
    for i in range(length):
        ruler += "....|"
    ruler += "\n"
    ruler += "0"
    for i in range(1, length + 1):
        ruler += f"{i:5}"
    return ruler


def make_meter(length, width):
    meter = ""
    for j in range(length):
        for i in range(width):
            meter += "+---"
        meter += "+\n"
        for i in range(width):
            meter += "|   "
        meter += "|\n"
    for i in range(width):
        meter += "+---"
    meter += "+"
    return meter


if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        raise ValueError("Provide one argument or two arguments.")
    if len(sys.argv) == 2:
        print(make_ruler(int(sys.argv[1])))
    else:
        print(make_meter(int(sys.argv[1]), int(sys.argv[2])))
    exit(0)
