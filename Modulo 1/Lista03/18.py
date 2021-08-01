div = 0
res = 0

for x in reversed(range(2, 39)):
    div += 1
    res += ((x - 1) + (x)) / div
    print(((" +") if (div != 1) else ""), f" ({x - 1} * {x}/ {div})", end="")
print("\nResultado = " + str(res))