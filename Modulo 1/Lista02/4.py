Idade_dias = int(input("Quantos dias você tem de idade? "))
Ano = Idade_dias//365
Mes = (Idade_dias - (Ano * 365))//30
Dia = Idade_dias - ((Mes * 30) + (Ano * 365))
print("Sua idade é de {} anos, {} mêses e {} dias.".format(Ano, Mes, Dia))
