j=0
cont=0
while True:
    n = int(input())
    if n < 0:
        break
    if n %3==0:
        j += n
        cont +=1
print(j/cont)
