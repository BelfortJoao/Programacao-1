res = 0
n = 0
print("S= ", end="")
for n2 in range(1, 51):

    if n2 == 1:
        n += 1
        print(f"{n}/{n}", end="")
    else:
        n += 2
        res += (n / n2)
        print(f" + {n}/{n2}", end="")
print(f"\nResultado = {res}")
