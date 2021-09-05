N_testes=int(input())
for i in range (0,N_testes):
    Teste=input().split()
    Mao1=int(Teste[0])
    Mao2=int(Teste[1])
    if Mao1 ==1 and Mao2 == 1:
        print("coma")
    else:
        print("pense")
