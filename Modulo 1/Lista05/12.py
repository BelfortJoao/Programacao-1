x = int(input("Escreva um angulo: "))
x = x/180
cont=0
S=0
f=1
for i in range(3, 32, 2):
    for j in range(i, 0, -1):
        f*=j
    if cont == 0:
        S=(x-((x**i)/f))
        print(S)
    elif cont%2==0 and cont != 0:
        S= S +((x**i)/f)
    else:
        S =S+((x ** i) / f)
    cont +=1
    f = 1
    print(S)
print(S)
