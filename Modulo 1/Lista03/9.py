Total = 0
Cont = 0
while True:
    Num = int(input())
    if Num == -1:
        break
    if Num >= 0:
        Cont += 1
        Total += Num
print(Total / Cont)