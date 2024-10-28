str_input = int(input("How long do you want the meter to be? "))

for i in range(str_input):
    print(f"|....", end="")
print("|")
print("0", end="")
for i in range(str_input):
    print(f"{i+1:5}", end="")
