Idade = int(input("Qual é sua idade? "))
if 18 <= Idade < 65:
    print("Eleitor obrigatório")
elif Idade > 65 or 16 <= Idade < 18:
    print("Eleitor facultativo")
else:
    print("Não eleitor")