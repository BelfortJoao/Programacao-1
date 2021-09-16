matriz = [[0 for i in range(5)] for y in range(5)]
for j in range(5):
    for x in range(5):
        matriz[j][x] = int(input())
for x in range(5):
    print(matriz[x][5])