A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))
C = int(input("digite mais um número: "))
if A >= B and A >= C:
    print(f"{A},", end="")
    if B >= C:
        print(f"{B},{C}.")
    else:
        print(f"{C},{B}.")
if B >= A and B >= C:
    print(f"{B},", end="")
    if A >= C:
        print(f"{A},{C}.")
    else:
        print(f"{C},{A}.")
if C >= A and C >= B:
    print(f"{C},", end="")
    if A >= B:
        print(f"{A},{B}.")
    else:
        print(f"{B},{A}.")
