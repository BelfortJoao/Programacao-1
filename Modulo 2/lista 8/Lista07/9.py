import random
matriz = [[0 for i in range(3)] for y in range(4)]
for i in range(3):
    for j in range(4):
        matriz[i][j] = random.randint(0, 10)
for i in range(3):
    for j in range(4):
        matriz[i][j] = matriz[i][j] *3
print(matriz)
