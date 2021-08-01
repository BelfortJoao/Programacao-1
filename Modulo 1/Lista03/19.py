res = num = 1
print(res, end="")
for x in range(1, 52):
    num += 2
    if (x % 2) == 0:
        res += (1 / (num ** 3))
        print(f" + 1/{num}³", end="")
    else:
        res -= (1 / (num ** 3))
        print(f" - 1/{num}³", end="")
print(f"""
Resultado =   {res} 
Resultado de π = {((res * 32) ** 1 / 3)}""")
