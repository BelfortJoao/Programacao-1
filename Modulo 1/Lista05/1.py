peso, alt =[int(input()) for x in range(0,2)]
print(peso)
print(alt)
IMC = peso / alt **2
print(IMC)
if IMC < 20:
    print("Abaixo do peso")
elif 20 < IMC < 25:
    print("Peso Normal")
elif 25 < IMC < 30:
    print("Sobrepeso")
elif 30 < IMC < 40:
    print("Obeso")
elif 40 < IMC:
    print("Obeso Mórbido")

