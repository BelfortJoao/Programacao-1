MaiorH=0
MaiorH_nome = ""
MaiorP=0
MaiorP_nome = ""
It= 0
cont= 0
while True:
    N= input("nome: ")
    S=input("sexo[F/M]: ").upper()
    I = int(input("idade[H]: "))
    P = int(input("peso: "))
    H = int(input("altura: "))
    if N == "@":
        break
    if S == "M" and H > MaiorH:
        MaiorH=H
        MaiorH_nome=N
    if S == "F" and P > MaiorP:
        MaiorP=P
        MaiorP_nome=N
    It += I
    cont+=1
print(f"""O atleta do sexo masculino mais alto:{MaiorH}
A atleta do sexo feminino mais pesada:{MaiorP}
A média de idade dos atletas:{It/cont}
""")

