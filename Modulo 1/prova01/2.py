indentificador=int(input())
cont = 0
n1 = 1
n2 = 1
n3 = 0
if indentificador == 1:
    print("ganso")
else:
    while n3 < indentificador:
        n3 = n1 + n2
        n1 = n2
        t2 = n3
        cont += 1
        if n1 < indentificador <= n3:
            if cont%2 ==0:
                print("pato")
            else:
                print("ganso")
