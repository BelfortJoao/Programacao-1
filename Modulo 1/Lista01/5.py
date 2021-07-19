from math import pow
h = int(input("Qual a altura? "))
R = int(input("Qual o raio? "))
V = 3.14159 * pow(R,2) * h
print("--------------------------------------- \n O volume é de {:.2f} \n --------------------------------------- ".format(V))