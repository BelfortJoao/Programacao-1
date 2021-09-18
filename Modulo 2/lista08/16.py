loja = [[int(input(f"{i + 1}° mês | {j + 1}° sem - valor: ")) for j in range(4)] for i in range(12)]
tot, m = 0, []

for mes in range(len(loja)):
    m.append(loja[mes][0])
    for sem in range(len(loja[mes])):
        m[mes] += loja[mes][sem]
        tot += loja[mes][sem]

print(f"Ano: R${tot}")
for i in range(len(loja)):
    print(f"{i + 1}° Mês: R${m[i]}")
    for j in range(len(loja[i])): print(f"  {j + 1}° Sem: R${loja[i][j]}")