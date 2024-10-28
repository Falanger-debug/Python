def roman2int(roman):
    letters = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    n = len(roman)
    for i in range(n):
        if i < n - 1 and letters[roman[i]] < letters[roman[i + 1]]:
            result -= letters[roman[i]]
        else:
            result += letters[roman[i]]
    return result


roman_example = "MCMXCIV"

print(f"For the roman number {roman_example} the integer value is: {roman2int(roman_example)}")

# inne sposoby na tworzenie takiego słownika

letters1 = dict([
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000)
])

keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
letters_2 = dict(zip(keys, values))
