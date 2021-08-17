A=5000000
B=7000000
cont=0
while True:
    if B < A:
        break
    else:
        A*=1.03
        B*=1.02
    cont +=1
print(f"{cont} anos")