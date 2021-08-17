tot = 0

while True:
    N = int(input("Número pedido: "))
    if N == 0:
        break
    input("Data pedido: ")
    P = float(input("Preço unitário: "))
    qtd = int(input("Quantidade: "))
    tot += qtd * P
print("Valor total: R${:.2f}".format(tot))