import random
matriz = [[0 for i in range(10)] for y in range(10)]
S = 0
for i in range(10):
    for j in range(10):
        matriz[i][j] = random.randint(0, 10)
for i in range(10):
    for j in range(9, -1, -1):
        if i + j != 9:
            print(matriz[i][j])
print(matriz)




