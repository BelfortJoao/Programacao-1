from math import sqrt
N1 = float(input("Escreva um número: "))
N2 = float(input("Escreva outro número: "))
if N1 > N2 :
    print("A raiz quadrada de {} é {}\nO quadrado de {} é {}".format(N1, sqrt(N1), N2, N2**2))
else:
    print("A raiz quadrada de {} é {}\nO quadrado de {} é {}".format(N2, sqrt(N2), N1, N1**2))