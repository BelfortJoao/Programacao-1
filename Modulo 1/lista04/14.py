from math import sqrt
Numero = float(input("Escreva um número: "))
if Numero >= 0:
    print("A raiz quadrada de {:.2f} é {}".format(Numero, sqrt(Numero)))
else:
    print("O quadrado de {} é {}".format(Numero, Numero**2))