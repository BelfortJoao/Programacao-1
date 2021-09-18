Tam=int(input("Tamanho dos vetores: "))
Vetor1=[int(input(f"{i+1}º numero do vetor 1: ")) for i in range(Tam)]
Vetor2=[int(input(f"{i+1}º numero do vetor 2: ")) for i in range(Tam)]
Vetor3=[0 for i in range(Tam*2)]
for i in range(Tam):
    if i < Tam//2:
        if i % 2 == 0:
            Vetor3[i] = Vetor1[i]
        else:
            Vetor3[i] = Vetor2[i - 1]
    else:
        if i % 2 == 0:
            Vetor3[i] = Vetor1[i+(Tam//2)]
        else:
            Vetor3[i] = Vetor2[i - 1+(Tam//2)]

print(Vetor3)