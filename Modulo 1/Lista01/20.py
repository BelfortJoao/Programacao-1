#Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:
#Não eleitor (abaixo de 16 anos);
# (entre a faixa de 18 e menor de 65 anos);
#Eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive).
Idade = int(input("Qual é sua idade? "))
if 18 <= Idade < 65:
    print("Eleitor obrigatório")
elif Idade > 65 or 16 <= Idade < 18:
    print("Eleitor facultativo")
else:
    print("Não eleitor")