Tempo = int(input("Quanto tempo foi gasto em minutos? "))
Velocidade = int(input("Qual foi sua velocidade(Em Km/h)? "))
Distância = Tempo * Velocidade
Litros = Distância / 12
print("--------------------------------------- \n Você percorreu {:.2f}Km \n E gastou {:.2f} Litros \n --------------------------------------- ".format( Distância, Litros ))