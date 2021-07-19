Despesas = float(input("Quanto foi gasto?"))
Gorjeta = Despesas / 100 * 10
Total = Despesas + Gorjeta
print("--------------------------------------- \n O total foi de R${:.2f} \n Com uma gorjeta de R${:.2f} \n --------------------------------------- ".format(Total, Gorjeta))
