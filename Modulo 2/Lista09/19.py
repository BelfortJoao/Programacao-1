# Escreva um algoritmo para determinar se um número A é divisível por um outro número B. Esses valores devem ser fornecidos pelo usuário.
Num1 = int(input("Digite um numero: "))
Num2 = int(input("digite outro numero: "))
if Num1 > Num2:
    print("o {} é maior do que {}".format(Num1, Num2))
elif Num1 < Num2:
    print("o {} é menor do que {}".format(Num1, Num2))
else:
    print("o {} é igual à {}".format(Num1, Num2))


