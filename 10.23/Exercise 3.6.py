length = int(input("How long do you want the meter to be? "))
width = int(input("How wide do you want the meter to be? "))

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
print(meter)
