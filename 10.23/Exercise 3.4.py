while True:
    str_input = input("Enter a number in a form such as: 123.456: ").lower()
    if str_input == 'stop':
        break
    num = float(str_input)

    try:
        num = float(str_input)
        print(f"The number you entered is: {num} and its cube is {num ** 3}")
    except ValueError:
        print("Please enter a number in the correct form.")
        continue
