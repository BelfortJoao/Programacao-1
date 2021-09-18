import random
matriz = [[0 for i in range(10)] for y in range(10)]
for i in range(10):
    for j in range(10):
        matriz[i][j] = random.randint(0, 10000)
n = 0
for i in range(10):
    n += 1
    for j in range(n):
        print(matriz[i][j])
print(matriz)