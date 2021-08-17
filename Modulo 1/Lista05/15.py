A, B, C, D, E, cont, ip, io, ir = 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in range(0,6):
    idade = int(input(f"qual sua idade: "))
    Opin = str(input("""
Escreva qual notá você da ao filme de acordo com a tabela
|Nota | Significado |
|A    | Ótimo       | 
|B    | Bom         |
|C    | Regular     |
|D    | Ruim        | 
|E    | Péssimo     |
Nota: """)).upper()
    if Opin == "A":
        A += 1
        if idade >= io:
            io = idade
    if Opin == "B":
        B += 1
    if Opin == "C":
        C += 1
    if Opin == "D":
        D += 1
        if idade >= ir:
            ir = idade
    if Opin == "E":
        E += 1
        if idade >= ip:
            ip = idade
    cont += 1
    print(" " * 10)
print(f"""Respostas ótimas: {A}
Diferença entre bom e regular: {((B-C*100)/cont)}%
Quantidade de pessoas que utilizou pessimo: {E}
Pessoas mais velha que utilizou pessimo: {ip}
Diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim: {io-ir}""")
