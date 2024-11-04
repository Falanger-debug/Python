import sys

def make_ruler(n):

    if type(n) != int:
        raise ValueError("Input must be an integer")
    result ="|"
    for i in range(n):
        result += "....|"
    result += "\n"
    result += "0"
    for i in range(1, n + 1):
        result += f"{i:5}"
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 make_ruler.py <n>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        print(make_ruler(n))
    except ValueError:
        print("Error: <n> must be an integer.")
        sys.exit(1)