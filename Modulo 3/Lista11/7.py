matriz = [[0 for i in range(4)] for y in range(10)]
for j in range(50):
    matriz[1][j] = input("Matricula: ")
    matriz[2][j] = int(input("Sexo(0- Feminino 1-Masculino): "))
    split = matriz[1][j].split()
    matriz[3][j] = split[3]+split[4]+split[5]
    matriz[4][j] = int(input("CR: "))
Maior = 0
M = 0
for j in range(50):

    if matriz[4][j] > Maior:
        if matriz[2][j]==0:
            Maior = matriz[4][j]
            M = j
print(f"{matriz[1][M]},{matriz[4][M]},{matriz[3][M]} ")
