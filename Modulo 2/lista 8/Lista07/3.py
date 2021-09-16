matriz = [[0 for i in range(5)] for y in range(7)]
for i in range(7):
    for j in range(5):
        matriz[i][j] = int(input())
for i in range(7):
    for j in range(5):
        if matriz[i][j]%2 != 0:
            matriz[i][j] = matriz[i][j]*2
print(matriz)

