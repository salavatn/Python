import random

with open(file=r"content\middle_names.txt") as file:
    names = file.read().split()

count = len(names)
num = random.randint(0, count-1)


def req_hostname():
    if num < 10:
        return f"FP00{num}_{names[num].upper()}"
    elif num < 100:
        return f"FP0{num}_{names[num].upper()}"
    elif num >= 100:
        return f"FP{num}_{names[num].upper()}"


req_hostname()
