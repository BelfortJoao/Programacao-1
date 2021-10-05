#Construa um algoritmo que leia dois valores numéricos e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.
Num1 = int(input("Digite um numero:"))
Num2 = int(input("Digite outro numero:"))
Soma = Num1 + Num2
if Soma > 10:
    print("A soma é igual a {}".format(Soma))