X = 0
x = []
y = []
soma = 0
while True:
    x.append(int(input(f"{X+1}º Id: ")))
    y.append(int(input(f"{X+1}º valor a pagar: ")))
    if x[X] < 0:
        break
    X += 1
print("    Id    | Valores ")
for i in range(X+1):
    print(f" {x[i]}  |  {y[i]} ")
    soma += y[i]
print(f"Valor total do caixa: {soma}")