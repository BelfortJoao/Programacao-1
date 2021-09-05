x = [int(input()) for x in range(25)]
n = int(input())
y = 0
for i in range(25):
    if x[i] == n:
        print(f"O número {x[i]} está na posição {i}")
    else:
        y += 1
if y == 25 :
    print("Erro: número não encontrado")
