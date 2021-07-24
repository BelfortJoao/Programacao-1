Peso_Ter=float(input("Informe seu peso: "))
Escolha = int(input(""""
Escolha um planeta:
1) Mercúrio
2) Vênus
3) Marte
4) Júpiter
5) Saturno
6) Urano
: """))
if Escolha == 1:
    print("O seu peso em Mercúrio é igual a {:.3f}Kg".format(Peso_Ter * 0.37))
elif Escolha == 2:
    print("O seu peso em Vênus é igual a {:.3f}Kg".format(Peso_Ter * 0.88))
elif Escolha == 3:
    print("O seu peso em Marte é igual a {:.3f}Kg".format(Peso_Ter * 0.38))
elif Escolha == 4:
    print("O seu peso em Júpiter é igual a {:.3f}Kg".format(Peso_Ter * 2.64))
elif Escolha == 5:
    print("O seu peso em Saturno é igual a {:.3f}Kg".format(Peso_Ter * 1.15))
elif Escolha == 6:
    print("O seu peso em Urano é igual a {:.3f}Kg".format(Peso_Ter * 1.17))
else:
    print("Escolha Invalida")
