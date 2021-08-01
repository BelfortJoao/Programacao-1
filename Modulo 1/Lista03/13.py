n2 = 0
n3 = 1
while True:
    n = int(input("digite um número : "))
    if n <= 0:
        break
    else:
        if n%2 == 0:
            n2 +=n
        elif n%2 != 0:
            n3 *= n
print(f"produto: {n3}")
print(f"soma: {n2}")


