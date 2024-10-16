line = ("Lorem ipsum GvR dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et "
        "dolore"
        "magna GvR d Gv   Gvr G vR raliqua.")


def change_GvR_to_Guido_van_Rossum(line):
    return line.replace("GvR", "Guido van Rossum")


print(change_GvR_to_Guido_van_Rossum(line))
