A=0
B=0
cont=0
while True:
    if A+B== 2000 and cont!=0:
        break
    else:
        A+= 10
        B+= 15
    cont +=1
print(f"""distancia percorrida por
Ciclista A: {A}
Ciclista B: {B}""")