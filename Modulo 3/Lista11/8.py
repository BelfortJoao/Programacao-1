import random
matriz = [[0 for i in range(10)] for y in range(10)]
for i in range(10):
    for j in range(10):
        matriz[i][j] = random.randint(0, 10000)
guarda1=guarda2=guarda3=[0 for i in range(10)]

for j in range(10):
    guarda1[j] = matriz[2][j]
    matriz[2][j] = matriz[8][j]
    matriz[8][j] = guarda1[j]
for j in range(10):
    guarda2[j] = matriz[4][j]
    matriz[4][j] = matriz[10][j]
    matriz[10][j] = guarda2[j]
n = 9
for j in range(10):
    guarda3[j] = matriz[j][j]
    matriz[j][j] = matriz[n][j]
    matriz[n][j] = guarda3[j]
    n -= 1

print(matriz)
