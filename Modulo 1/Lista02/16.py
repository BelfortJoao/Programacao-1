Mes = int(input("Escreva um numero de um mês: "))
if 1 <= Mes <= 3:
    print("1° trimestre")
elif 3 < Mes <= 6:
    print("2° trimestre")
elif 6 < Mes <= 9:
    print("3° trimestre")
elif 9 < Mes <= 12:
    print("4° trimestre")
else:
    print("Mês inválido")
