sal = 500.00
nom = str(input("Digite o nome do vendedor: "))
car_Ven = int(input("Quantidade de carros vendidos: "))
val_tot = float(input("Valor total das vendas: R$"))
sal_tot = sal + (car_Ven * 50.00) + (val_tot * (5 / 100))
print("Salário total de  {} +  é R${:.2f}.".format(nom, sal_tot))
