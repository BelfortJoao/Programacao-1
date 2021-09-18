n = int(input("Qual o tamanho do vetor?"))
x = [int(input()) for x in range(n)]
for i in range(0, n, 2):
    print(x[i])
