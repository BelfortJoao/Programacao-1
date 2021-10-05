# Escreva um algoritmo para determinar se um número A é divisível por um outro número B. Esses valores devem ser fornecidos pelo usuário.
Num1 = int(input("Digite um numero: "))
Num2 = int(input("digite outro numero: "))
if Num1 % Num2 > 0 :
    print("{} não é divisivel por {}".format(Num1, Num2))
else:
    print("{} é divisivel por {}".format(Num1, Num2))
