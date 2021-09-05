Preco_tot=0
Peso_tot=0
quan = int(input("A quantidade de caixas descarregadas: "))
Peso = [float(input(f"O peso das caixa {i+1}: ")) for i in range(quan)]
Preco = [float(input(f"O peso das caixa {i+1}: ")) for i in range(quan)]
Val = float(input("Valor monetário total da carga: "))
for i in range(quan):
    Preco_tot += Preco[i]
    Peso_tot += Peso[i]
if Preco_tot != Val:
    print(f"O valor de carga retirado de R${Preco_tot} não condiz com o Valor total de R${Val}")
print(f"Peso total: {Peso}Kg \n Preço total: {Preco}")
