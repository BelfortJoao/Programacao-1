matriz = [[0 for i in range(7)] for y in range(7)]
stop=0
for i in range(7):
    for j in range(7):
        matriz[i][j] = int(input())
n = int(input())
for i in range(7):
    for j in range(7):
        if matriz[i][j] == n:
            print(n)
            stop += 1
if stop != 0:
    print('error')
