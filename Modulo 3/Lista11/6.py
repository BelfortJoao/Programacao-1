matriz = [[0 for i in range(3)] for y in range(50)]
for j in range(50):
    matriz[1][j] = input("Nome:")
    matriz[2][j] = int(input("Estoque Ideal:"))
    matriz[3][j] = int(input("estoque atual:"))
D=0
print("Lista de compras")
for j in range(50):
    D = matriz[2][j]-matriz[3][j]
    if D >0:
        print(f"-Planta {matriz[1][j]} precisa de mais {D} unidades.", end=""
                                                                    "")
    D = 0
print(matriz)
